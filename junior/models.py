from django.db import models
from django.contrib.auth.models import User

class FirstTerm(models.Model):
    session = models.ForeignKey('management.Session', on_delete = models.SET_NULL, default=1, null=True, related_name="junior_session")
    student = models.OneToOneField('records.student', on_delete = models.SET_NULL, unique = True, null=True, related_name="junior_student")
    school_fees = models.BooleanField(max_length=5, default = False)
    quran_ca = models.IntegerField(blank=True, default = 0, verbose_name="القرآن (الإختبار)")
    tajweed_ca = models.IntegerField(blank=True, default = 0, verbose_name="التجويد (الإختبار)")
    mutoolaah_ca = models.IntegerField(blank=True, default = 0, verbose_name="المطالعة (الإختبار)")
    arabiyyah_ca = models.IntegerField(blank=True, default = 0, verbose_name="العربية (الإختبار)")
    nahw_ca = models.IntegerField(blank=True, default = 0, verbose_name="النحو (الإختبار)")
    tawheed_ca = models.IntegerField(blank=True, default = 0, verbose_name="التوحيد (الإختبار)")
    fiqh_ca = models.IntegerField(blank=True, default = 0, verbose_name="الفقه (الإختبار)")
    seeroh_ca = models.IntegerField(blank=True, default = 0, verbose_name="السيرة (الإختبار)")
    hadeeth_ca = models.IntegerField(blank=True, default = 0, verbose_name="الحديث (الإختبار)")
    nusuus_ca = models.IntegerField(blank=True, default = 0, verbose_name="النصوص (الإختبار)")
    tabeer_ca = models.IntegerField(blank=True, default = 0, verbose_name="التعبير (الإختبار)")
    duruusu_ca = models.IntegerField(blank=True, default = 0, verbose_name="دروس اللغة (الإختبار)")
    hadeethulhifz_ca = models.IntegerField(blank=True, default = 0, verbose_name="حديث الحفظ (الإختبار)")


    quran_exam = models.IntegerField(blank=True, default = 0, verbose_name="القرآن (الإمتحان)")
    tajweed_exam = models.IntegerField(blank=True, default = 0, verbose_name="التجويد (الإمتحان)")
    mutoolaah_exam = models.IntegerField(blank=True, default = 0, verbose_name="المطالعة (الإمتحان)")
    arabiyyah_exam = models.IntegerField(blank=True, default = 0, verbose_name="العربية (الإمتحان)")
    nahw_exam = models.IntegerField(blank=True, default = 0, verbose_name="النحو (الإمتحان)")
    tawheed_exam = models.IntegerField(blank=True, default = 0, verbose_name="التوحيد (الإمتحان)")
    fiqh_exam = models.IntegerField(blank=True, default = 0, verbose_name="الفقه (الإمتحان)")
    seeroh_exam = models.IntegerField(blank=True, default = 0, verbose_name="السيرة (الإمتحان)")
    hadeeth_exam = models.IntegerField(blank=True, default = 0, verbose_name="الحديث (الإمتحان)")
    nusuus_exam = models.IntegerField(blank=True, default = 0, verbose_name="النصوص (الإمتحان)")
    tabeer_exam = models.IntegerField(blank=True, default = 0, verbose_name="التعبير (الإمتحان)")
    duruusu_exam = models.IntegerField(blank=True, default = 0, verbose_name="دروس اللغة (الإمتحان)")
    hadeethulhifz_exam = models.IntegerField(blank=True, default = 0, verbose_name="حديث الحفظ (الإمتحان)")

    quran_tot = models.IntegerField(blank=True, default = 0)
    tajweed_tot = models.IntegerField(blank=True, default = 0)
    mutoolaah_tot = models.IntegerField(blank=True, default = 0)
    arabiyyah_tot = models.IntegerField(blank=True, default = 0)
    nahw_tot = models.IntegerField(blank=True, default = 0)
    tawheed_tot = models.IntegerField(blank=True, default = 0)
    fiqh_tot = models.IntegerField(blank=True, default = 0)
    seeroh_tot = models.IntegerField(blank=True, default = 0)
    hadeeth_tot = models.IntegerField(blank=True, default = 0)
    nusuus_tot = models.IntegerField(blank=True, default = 0)
    tabeer_tot = models.IntegerField(blank=True, default = 0)
    duruusu_tot = models.IntegerField(blank=True, default = 0)
    hadeethulhifz_tot = models.IntegerField(blank=True, default = 0)
    cumulative = models.IntegerField(blank=True, default = 0)
    teacher_comment = models.CharField(max_length=200, null=True, blank=True, verbose_name="تعليق المدرس")
    head_comment = models.CharField(max_length=200, null=True, blank=True, verbose_name="تعليق المدير")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('student__user__username',)
        verbose_name = "First Term Score"
        verbose_name_plural = "First Term Scores"

    def grade_quran(self):
        if self.quran_tot < 40:
            return "F - Fail"
        elif self.quran_tot >= 40 and self.quran_tot < 45:
            return "E - Weak Pass"
        elif self.quran_tot >= 45 and self.quran_tot < 50:
            return "D - Fair"
        elif self.quran_tot >= 50 and self.quran_tot < 60:
            return "C - Good"
        elif self.quran_tot >= 60 and self.quran_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_tajweed(self):
        if self.tajweed_tot < 40:
            return "F - Fail"
        elif self.tajweed_tot >= 40 and self.tajweed_tot < 45:
            return "E - Weak Pass"
        elif self.tajweed_tot >= 45 and self.tajweed_tot < 50:
            return "D - Fair"
        elif self.tajweed_tot >= 50 and self.tajweed_tot < 60:
            return "C - Good"
        elif self.tajweed_tot >= 60 and self.tajweed_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_mutoolaah(self):
        if self.mutoolaah_tot < 40:
            return "F - Fail"
        elif self.mutoolaah_tot >= 40 and self.mutoolaah_tot < 45:
            return "E - Weak Pass"
        elif self.mutoolaah_tot >= 45 and self.mutoolaah_tot < 50:
            return "D - Fair"
        elif self.mutoolaah_tot >= 50 and self.mutoolaah_tot < 60:
            return "C - Good"
        elif self.mutoolaah_tot >= 60 and self.mutoolaah_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_arabiyyah(self):
        if self.arabiyyah_tot < 40:
            return "F - Fail"
        elif self.arabiyyah_tot >= 40 and self.arabiyyah_tot < 45:
            return "E - Weak Pass"
        elif self.arabiyyah_tot >= 45 and self.arabiyyah_tot < 50:
            return "D - Fair"
        elif self.arabiyyah_tot >= 50 and self.arabiyyah_tot < 60:
            return "C - Good"
        elif self.arabiyyah_tot >= 60 and self.arabiyyah_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_nahw(self):
        if self.nahw_tot < 40:
            return "F - Fail"
        elif self.nahw_tot >= 40 and self.nahw_tot < 45:
            return "E - Weak Pass"
        elif self.nahw_tot >= 45 and self.nahw_tot < 50:
            return "D - Fair"
        elif self.nahw_tot >= 50 and self.nahw_tot < 60:
            return "C - Good"
        elif self.nahw_tot >= 60 and self.nahw_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_tawheed(self):
        if self.tawheed_tot < 40:
            return "F - Fail"
        elif self.tawheed_tot >= 40 and self.tawheed_tot < 45:
            return "E - Weak Pass"
        elif self.tawheed_tot >= 45 and self.tawheed_tot < 50:
            return "D - Fair"
        elif self.tawheed_tot >= 50 and self.tawheed_tot < 60:
            return "C - Good"
        elif self.tawheed_tot >= 60 and self.tawheed_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_fiqh(self):
        if self.fiqh_tot < 40:
            return "F - Fail"
        elif self.fiqh_tot >= 40 and self.fiqh_tot < 45:
            return "E - Weak Pass"
        elif self.fiqh_tot >= 45 and self.fiqh_tot < 50:
            return "D - Fair"
        elif self.fiqh_tot >= 50 and self.fiqh_tot < 60:
            return "C - Good"
        elif self.fiqh_tot >= 60 and self.fiqh_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_seeroh(self):
        if self.seeroh_tot < 40:
            return "F - Fail"
        elif self.seeroh_tot >= 40 and self.seeroh_tot < 45:
            return "E - Weak Pass"
        elif self.seeroh_tot >= 45 and self.seeroh_tot < 50:
            return "D - Fair"
        elif self.seeroh_tot >= 50 and self.seeroh_tot < 60:
            return "C - Good"
        elif self.seeroh_tot >= 60 and self.seeroh_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_hadeeth(self):
        if self.hadeeth_tot < 40:
            return "F - Fail"
        elif self.hadeeth_tot >= 40 and self.hadeeth_tot < 45:
            return "E - Weak Pass"
        elif self.hadeeth_tot >= 45 and self.hadeeth_tot < 50:
            return "D - Fair"
        elif self.hadeeth_tot >= 50 and self.hadeeth_tot < 60:
            return "C - Good"
        elif self.hadeeth_tot >= 60 and self.hadeeth_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_nusuus(self):
        if self.nusuus_tot < 40:
            return "F - Fail"
        elif self.nusuus_tot >= 40 and self.nusuus_tot < 45:
            return "E - Weak Pass"
        elif self.nusuus_tot >= 45 and self.nusuus_tot < 50:
            return "D - Fair"
        elif self.nusuus_tot >= 50 and self.nusuus_tot < 60:
            return "C - Good"
        elif self.nusuus_tot >= 60 and self.nusuus_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_tabeer(self):
        if self.tabeer_tot < 40:
            return "F - Fail"
        elif self.tabeer_tot >= 40 and self.tabeer_tot < 45:
            return "E - Weak Pass"
        elif self.tabeer_tot >= 45 and self.tabeer_tot < 50:
            return "D - Fair"
        elif self.tabeer_tot >= 50 and self.tabeer_tot < 60:
            return "C - Good"
        elif self.tabeer_tot >= 60 and self.tabeer_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_duruusu(self):
        if self.duruusu_tot < 40:
            return "F - Fail"
        elif self.duruusu_tot >= 40 and self.duruusu_tot < 45:
            return "E - Weak Pass"
        elif self.duruusu_tot >= 45 and self.duruusu_tot < 50:
            return "D - Fair"
        elif self.duruusu_tot >= 50 and self.duruusu_tot < 60:
            return "C - Good"
        elif self.duruusu_tot >= 60 and self.duruusu_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_hadeethulhifz(self):
        if self.hadeethulhifz_tot < 40:
            return "F - Fail"
        elif self.hadeethulhifz_tot >= 40 and self.hadeethulhifz_tot < 45:
            return "E - Weak Pass"
        elif self.hadeethulhifz_tot >= 45 and self.hadeethulhifz_tot < 50:
            return "D - Fair"
        elif self.hadeethulhifz_tot >= 50 and self.hadeethulhifz_tot < 60:
            return "C - Good"
        elif self.hadeethulhifz_tot >= 60 and self.hadeethulhifz_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_general(self):
        if self.cumulative/13 < 40:
            return "F - Fail"
        elif self.cumulative/13 >= 40 and self.mustolah_ulhadeeth_tot < 45:
            return "E - Weak Pass"
        elif self.cumulative/13 >= 45 and self.mustolah_ulhadeeth_tot < 50:
            return "D - Fair"
        elif self.cumulative/13 >= 50 and self.mustolah_ulhadeeth_tot < 60:
            return "C - Good"
        elif self.cumulative/13 >= 60 and self.mustolah_ulhadeeth_tot < 70:
            return "B - Very Good"
        else:
            return "Excellent"

    def cum_perc(self):
        return str(round((self.cumulative/13),4))
