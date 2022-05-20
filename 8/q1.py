import sqlite3
from datetime import datetime

import requests
import xmltodict as xmltodict


def strToDatatime2(str):
    year = int(str[:4])
    month = int(str[5:7])
    day = int(str[8:10])
    hour = int(str[11:13])
    min = int(str[14:16])
    sec = int(str[17:19])
    return datetime(year, month, day, hour, min, sec)


def val(title, content, type, text: False):
    try:
        try:
            content[title]['@m:null']
        except:
            if text:
                element = content[title]['#text']
            else:
                element = content[title]
            if element == '@null':
                return None
            return type(element)
    except:
        return None


if __name__ == '__main__':
    response = requests.get('https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_Committee()')
    # returns an XML file in order to parse I'm using xmltodict
    # solution from https://stackoverflow.com/questions/18308529/python-requests-package-handling-xml-response
    dict_data = xmltodict.parse(response.content)

    # creating new db and new table
    db = sqlite3.connect('my_database.db')
    cursor = db.cursor()
    cursor.execute(
        '''
        CREATE TABLE KNS_Committee(
        CommitteeID integer primary key, Name varchar (250), CategoryID integer, CategoryDesc varchar (150),
        KnessetNum integer, CommitteeTypeID integer, CommitteeTypeDesc varchar (125), Email varchar (254) ,
         StartDate datetime2, FinishDate datetime2, AdditionalTypeID integer , AdditionalTypeDesc varchar (125),
         ParentCommitteeID integer, CommitteeParentName varchar (250), IsCurrent bit , LastUpdatedDate datetime2
            )
        '''
    )
    print('(מספר מזהה של הועדה, שם הועדה, מספר קטגוריה, שם קטגוריה, מספר כנסת, מספר סוג הועדה, שם סוג הועדה, מייל, '
          'זמן התחלה, זמן סיום, קוד סוג משנה של הוועדה, תיאור סוג משנה של הוועדה, קוד ועדת האם, תיאור ועדת האם, '
          'האם הוועדה פעילה?, תאריך עדכון אחרון)')
    for elem in dict_data['feed']['entry']:
        CommitteeID = int(elem['id'][-2:-1])
        content = elem['content']['m:properties']
        Name = val('d:Name', content, str, False)
        CategoryID = val('d:CategoryID', content, int, True)
        CategoryDesc = val('d:CategoryDesc', content, str, False)
        KnessetNum = val('d:KnessetNum', content, int, True)
        CommitteeTypeID = val('d:CommitteeTypeID', content, int, True)
        CommitteeTypeDesc = val('d:CommitteeTypeDesc', content, str, False)
        Email = val('d:Email', content, str, False)
        StartDate = val('d:StartDate', content, strToDatatime2, True)
        FinishDate = val('d:FinishDate', content, strToDatatime2, True)
        AdditionalTypeID = val('d:AdditionalTypeID', content, int, True)
        AdditionalTypeDesc = val('d:AdditionalTypeDesc', content, str, False)
        ParentCommitteeID = val('d:ParentCommitteeID', content, int, True)
        CommitteeParentName = val('d:CommitteeParentName', content, str, True)
        IsCurrent = val('d:IsCurrent', content, bool, True)
        if IsCurrent == 'true':
            IsCurrent = True
        LastUpdatedDate = val('d:LastUpdatedDate', content, strToDatatime2, True)
        vals = [CommitteeID, Name, CategoryID, CategoryDesc, KnessetNum, CommitteeTypeID,
                CommitteeTypeDesc, Email, StartDate, FinishDate, AdditionalTypeID, AdditionalTypeDesc,
                ParentCommitteeID,
                CommitteeParentName, IsCurrent, LastUpdatedDate]
        # got 'sqlite3, IntegrityError: UNIQUE constraint failed' error when used simple INSERT therefor used
        # INSERT OR IGNORE, solution from:
        # https://stackoverflow.com/questions/36518628/sqlite3-integrityerror-unique-constraint-failed-when-inserting-a-value
        cursor.execute('''
            INSERT OR IGNORE INTO KNS_Committee(CommitteeID,Name, CategoryID, CategoryDesc, KnessetNum, CommitteeTypeID,
            CommitteeTypeDesc, Email, StartDate, FinishDate, AdditionalTypeID, AdditionalTypeDesc, ParentCommitteeID,
             CommitteeParentName,IsCurrent, LastUpdatedDate) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', vals)
        cursor.execute('''
               SELECT * FROM KNS_Committee
               ''')
        for row in cursor:
            print(row)
