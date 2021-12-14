import decimal
from django.db import connection
import os
import django

def classroom_requirement_course_offer(semester, year):
    sections=[]
    with connection.cursor() as cursor:
       
        cursor.execute('''
        SELECT COUNT(*) AS Sections
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 1 AND 10
        AND semester =  %s
        AND year = %s
        UNION 
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 11 AND 20
        AND semester =  %s
        AND year = %s
        UNION 
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 21 AND 30
        AND semester =  %s
        AND year = %s
        UNION 
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 31 AND 35
        AND semester = %s
        AND year = %s
        UNION 
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 36 AND 40
        AND semester = %s
        AND year =  %s
        UNION 
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 41 AND 50
        AND semester = %s
        AND year =%s
        UNION 
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 51 AND 55
        AND semester =  %s
        AND year = %s
        UNION 
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 56 AND 65
        AND semester =  %s
        AND year = %s''',[semester,year,semester,year,semester,year,semester,year,semester,year,semester,year,semester,year,semester,year])
        sections=[]
        ro = cursor.fetchall()
        print(ro)
        for sec in ro:
            sec = (sec[0])
            print(sec)
            sections.append(sec) 
        return sections 


def IUB_resource(semester,year):
     with connection.cursor() as cursor:
       
        cursor.execute(
        ''' SELECT SUM(seasapp_section_t.enrolled) AS Enroller,
            COUNT(seasapp_section_t.sectionNo) AS Section,
            SUM(seasapp_room_t.roomSize)
            FROM seasapp_section_t,seasapp_course_t,seasapp_room_t
            WHERE seasapp_section_t.offeredCourseID_id = seasapp_course_t.offeredCourseID 
            AND seasapp_section_t.roomID_id = seasapp_room_t.roomID 
            AND seasapp_section_t.semester=%s
            AND seasapp_section_t.year=%s
            GROUP BY seasapp_course_t.schoolTitle_id;
        ''',[semester,year])
        sections = []
        enrolled = []
        roomcap = []
        waste = []
        percent = []
        ro = cursor.fetchall()
        print(ro)
        for roll,sec,room in ro:
            print(roll)
            sections.append(roll) 
            aven = int(roll/sec)
            print(aven)
            enrolled.append(aven)
            aver = int(room/sec)
            roomcap.append(aver)
            was = aver - aven
            waste.append(was)
            des=int((was*100)/aver)
            percent.append(des)
        usage = {
            'sections':sections,
            'enrolled':enrolled,
            'roomcap': roomcap,
            'waste':waste ,
            'percent':percent
        }
        print(usage)
        return usage 