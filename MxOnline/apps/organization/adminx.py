import xadmin

from .models import *


class CourseOrgAdmin(object):
    list_display = ["name","catgory","click_nums","fav_nums","address","city"]
    search_fields =  ["name","catgory","click_nums","fav_nums","address"]
    list_filter =  ["name","catgory","click_nums","fav_nums","address","city"]
    relfield_style = "fk-ajax"
    model_icon = "fa fa-h-square"


class CityDictAdmin(object):
    list_display = ["name","add_time"]
    search_fields = ["name"]
    list_filter = ["name","add_time"]
    model_icon = "fa fa-location-arrow"


class TeacherAdmin(object):
    list_diaplay = ["name","org","work_years","work_comfany","work_position","points","click_num","fav_num","add_time"]
    search_fields = ["name","org","work_years","work_comfany","work_position","points","click_num","fav_num"]
    list_filter = ["name","org","work_years","work_comfany","work_position","points","click_num","fav_num","add_time"]
    model_icon = "fa fa-user"


xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)