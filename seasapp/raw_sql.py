from django.db import connection
import os
import django

def classroom_requirement_course_offer(Sem, Year):
    with connection.cursor() as cursor:
       
        cursor.execute('''
        SELECT COUNT(*) AS Sections
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 1 AND 10
        AND semester = "Spring"
        AND year =2020
        UNION ALL
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 11 AND 20
        AND semester =  "Spring"
        AND year = 2020
        UNION ALL
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 21 AND 30
        AND semester =  "Spring"
        AND year = 2020
        UNION ALL
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 31 AND 35
        AND semester = "Spring"
        AND year = 2020
        UNION ALL
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 36 AND 40
        AND semester = "Spring"
        AND year =  2020
        UNION ALL
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 41 AND 50
        AND semester = "Spring"
        AND year =2020
        UNION ALL
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 51 AND 55
        AND semester =  "Spring"
        AND year = 2020
        UNION ALL
        SELECT COUNT(*)
        FROM seasapp_section_t 
        WHERE capacity BETWEEN 56 AND 65
        AND semester =  "Spring"
        AND year = 2020''')
        sections=[]
        ro = cursor.fetchall()
        print(ro)
        for sec in ro:
            sec = (sec[0])
            print(sec)
            sections.append(sec) 
        return sections 