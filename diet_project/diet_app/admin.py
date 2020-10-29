from django.contrib import admin
from .models import *
from django.db.models import Sum
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(ImportExportModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        super().save_model(request, obj, form, change)
    list_filter = ('username','email','is_dietitian','is_customer','is_active','is_admin')
    list_display = ('id','username','email','is_dietitian','is_customer','is_active','is_admin')
    search_fields = ('username','email','is_dietitian','is_customer','is_active','is_admin')

class UserDataAdmin(ImportExportModelAdmin):
    class Meta:
        verbose_name_plural = "Customer"
    list_filter = ('user','firstname','lastname','mobile_no','dietitian','plan','is_paid','is_chart_sent','plan_end_date')
    list_display=('user','firstname','lastname','mobile_no','dietitian','plan','is_paid','is_chart_sent','amount_paid','plan_end_date')

    search_fields = ('user__username','firstname','lastname','mobile_no','dietitian__firstname','plan__title','is_paid','is_chart_sent','plan_end_date')

    def amount_paid(self,obj):
        totalamount=payment.objects.filter(user_id=obj).aggregate(Sum('amount'))['amount__sum']
        return totalamount





admin.site.register(MyUser,MyUserAdmin)
admin.site.register(UserData,UserDataAdmin)





class PlansAdmin(ImportExportModelAdmin):



    def customers(self,obj):
        count=UserData.objects.filter(plan=obj.id).count()
        return count




    def revenue(self,obj):
        count=UserData.objects.filter(plan=obj.id).count()
        rev=count*obj.price
        return rev


    def Profit(self,obj):
        customers=UserData.objects.filter(plan=obj)
        for customer in customers:
            try:
                dietitian = customer.dietitian
                d_revenue=dietitian.revenue
                total_revenue = self.revenue(obj)
                profit= float(total_revenue) - float(d_revenue)
                obj.profit=profit
            except:
                profit = self.revenue(obj)


            return profit




    search_fields = ('title', 'description', 'price', 'is_healthissue', 'is_plusplan')
    list_display = ('id','title', 'description', 'price', 'is_healthissue', 'is_plusplan', 'customers', 'revenue','Profit')
    list_filter = ('title', 'description', 'price', 'is_healthissue', 'is_plusplan')


admin.site.register(Plans,PlansAdmin)
class dietitianAdmin(ImportExportModelAdmin):
    list_display = ('user', 'firstname', 'lastname', 'mobile_no', 'qualification', 'commission_smartplan','commission_smartplan_healthissue','commission_smartplusplan','commission_smartplusplan_healthissue','revenue')
    list_filter = ('user', 'firstname', 'lastname', 'mobile_no', 'qualification', 'commission_smartplan','commission_smartplan_healthissue','commission_smartplusplan','commission_smartplusplan_healthissue','revenue')
    search_fields = ('user__username','firstname', 'lastname', 'mobile_no', 'qualification', 'commission_smartplan','commission_smartplan_healthissue','commission_smartplusplan','commission_smartplusplan_healthissue','revenue')
admin.site.register(dietitian,dietitianAdmin)

class roomAdmin(ImportExportModelAdmin):
    list_display = ('id','name','created_by','created_at','meeting')
    list_filter = ('name','created_by','created_at','meeting')
    search_fields = ('name','created_by','created_at','meeting__id')

admin.site.register(Room,roomAdmin)

class messageAdmin(ImportExportModelAdmin):
    list_display = ('id','text','sender','room_id')
    list_filter = ('text','sender','room_id')
    search_fields = ('text','sender','room_id__id')

admin.site.register(Messages,messageAdmin)

class rmAdmin(ImportExportModelAdmin):
    list_display = ('id','room','username','is_member','added_by')
    list_filter = ('room','username','is_member','added_by')
    search_fields = ('room__id','username__firstname','is_member','added_by')

admin.site.register(Room_Member,rmAdmin)

class meetingAdmin(ImportExportModelAdmin):
    list_display = ('id','user','dietitian','date','time','end_time','status','type','room_id')
    list_filter = ('user','dietitian','date','time','end_time','status','type','room_id')
    search_fields = ('user__firstname','dietitian__firstname','date','time','end_time','status','type','room_id')


admin.site.register(meeting,meetingAdmin)

class contactAdmin(ImportExportModelAdmin):
    list_display = ('id','name','email','subject','message')
    list_filter = ('name','email','subject','message')
    search_fields = ('name','email','subject','message')

admin.site.register(Contact,contactAdmin)

class paymentAdmin(ImportExportModelAdmin):
    list_display = ('id','user_id','transaction_id','plan_id','amount','date','time')
    list_filter = ('id','user_id','transaction_id','plan_id','amount','date','time')
    search_fields = ('id','user_id__firstname','transaction_id','plan_id__title','amount')

admin.site.register(payment,paymentAdmin)

class feedAdmin(ImportExportModelAdmin):
    list_display = ('id','name','review','datetime','image')
    list_filter = ('name','review','datetime','image')
    search_fields = ('name','review','datetime','image')

admin.site.register(feedback,feedAdmin)

class healthdataAdmin(ImportExportModelAdmin):

    def workout_type(self,obj):
        types=Workout_type.objects.filter(user=obj)
        typelist=[]
        for t in types:
            typelist.append(t.type)
        return typelist

    list_display = ('userdata','workout','workout_type','workout_time','workout_time_inday','workout_day_inweek','want_to_achive','type','dishes','have_disease','supplements','about')
    list_filter = ('userdata','workout','workout_type','workout_time','workout_time_inday','workout_day_inweek','want_to_achive','type','dishes','have_disease','supplements','about')
    search_fields = ('userdata__firstname','workout','workout_time','workout_time_inday','workout_day_inweek','want_to_achive','type','dishes','have_disease','supplements','about')



admin.site.register(UserHealthData,healthdataAdmin)
class reportAdmin(ImportExportModelAdmin):
    list_display = ('id','user','old_weight','new_weight','query')
    list_filter = ('user','old_weight','new_weight','query')
    search_fields = ('user__firstname','old_weight','new_weight','query')

admin.site.register(Week_Report,reportAdmin)

class PosterAdmin(ImportExportModelAdmin):
    pass

admin.site.register(poster,PosterAdmin)


admin.site.site_header = "SastaDiet Admin"
admin.site.site_title = "SastaDiet Admin Portal"
admin.site.index_title = "Welcome to SastaDiet"


# Register your models here.
