from django.db import models
from django.contrib.auth.models import User

class FirstTerm(models.Model):
    session = models.ForeignKey('management.Session', on_delete = models.SET_NULL, default=1, null=True, related_name="secondary_session")
    student = models.OneToOneField('records.Student', on_delete = models.SET_NULL, unique = True, null=True, related_name="secondary_student")
    school_fees = models.BooleanField(max_length=5, default = False)
    quran_ca = models.IntegerField(blank=True, default = 0, verbose_name="القرآن (الإختبار)")
    tajweed_ca = models.IntegerField(blank=True, default = 0, verbose_name="التجويد (الإختبار)")
    nahw_ca = models.IntegerField(blank=True, default = 0, verbose_name="النحو (الإختبار)")
    sorf_ca = models.IntegerField(blank=True, default = 0, verbose_name="الصرف (الإختبار)")
    uluum_ulquran_ca = models.IntegerField(blank=True, default = 0, verbose_name="علوم القرآن (الإختبار)")
    balaagah_ca = models.IntegerField(blank=True, default = 0, verbose_name="البلاغة (الإختبار)")
    tawheed_ca = models.IntegerField(blank=True, default = 0, verbose_name="التوحيد (الإختبار)")
    farooid_ca = models.IntegerField(blank=True, default = 0, verbose_name="الفرائض (الإختبار)")
    fiqh_ca = models.IntegerField(blank=True, default = 0, verbose_name="الفقه (الإختبار)")
    taareekh_ca = models.IntegerField(blank=True, default = 0, verbose_name="التاريخ (الإختبار)")
    hadeeth_ca = models.IntegerField(blank=True, default = 0, verbose_name="الحديث (الإختبار)")
    aruud_ca = models.IntegerField(blank=True, default = 0, verbose_name="العروض (الإختبار)")
    mantiqoh_ca = models.IntegerField(blank=True, default = 0, verbose_name="المنطقة (الإختبار)")
    tafseer_ca = models.IntegerField(blank=True, default = 0, verbose_name="التفسير (الإختبار)")
    mustolah_ulhadeeth_ca = models.IntegerField(blank=True, default = 0, verbose_name="مصطلح الحديث (الإختبار)")

    quran_exam = models.IntegerField(blank=True, default = 0, verbose_name="القرآن (الإمتحان)")
    tajweed_exam = models.IntegerField(blank=True, default = 0, verbose_name="التجويد (الإمتحان)")
    nahw_exam = models.IntegerField(blank=True, default = 0, verbose_name="النحو (الإمتحان)")
    sorf_exam = models.IntegerField(blank=True, default = 0, verbose_name="الصرف (الإمتحان)")
    uluum_ulquran_exam = models.IntegerField(blank=True, default = 0, verbose_name="علوم القرآن (الإمتحان)")
    balaagah_exam = models.IntegerField(blank=True, default = 0, verbose_name="البلاغة (الإمتحان)")
    tawheed_exam = models.IntegerField(blank=True, default = 0, verbose_name="التوحيد (الإمتحان)")
    farooid_exam = models.IntegerField(blank=True, default = 0, verbose_name="الفرائض (الإمتحان)")
    fiqh_exam = models.IntegerField(blank=True, default = 0, verbose_name="الفقه (الإمتحان)")
    taareekh_exam = models.IntegerField(blank=True, default = 0, verbose_name="التاريخ (الإمتحان)")
    hadeeth_exam = models.IntegerField(blank=True, default = 0, verbose_name="الحديث (الإمتحان)")
    aruud_exam = models.IntegerField(blank=True, default = 0, verbose_name="العروض (الإمتحان)")
    mantiqoh_exam = models.IntegerField(blank=True, default = 0, verbose_name="المنطقة (الإمتحان)")
    tafseer_exam = models.IntegerField(blank=True, default = 0, verbose_name="التفسير (الإمتحان)")
    mustolah_ulhadeeth_exam = models.IntegerField(blank=True, default = 0, verbose_name="مصطلح الحديث (الإمتحان)")

    quran_tot = models.IntegerField(blank=True, default = 0)
    tajweed_tot = models.IntegerField(blank=True, default = 0)
    nahw_tot = models.IntegerField(blank=True, default = 0)
    sorf_tot = models.IntegerField(blank=True, default = 0)
    uluum_ulquran_tot = models.IntegerField(blank=True, default = 0)
    balaagah_tot = models.IntegerField(blank=True, default = 0)
    tawheed_tot = models.IntegerField(blank=True, default = 0)
    farooid_tot = models.IntegerField(blank=True, default = 0)
    fiqh_tot = models.IntegerField(blank=True, default = 0)
    taareekh_tot = models.IntegerField(blank=True, default = 0)
    hadeeth_tot = models.IntegerField(blank=True, default = 0)
    aruud_tot = models.IntegerField(blank=True, default = 0)
    mantiqoh_tot = models.IntegerField(blank=True, default = 0)
    tafseer_tot = models.IntegerField(blank=True, default = 0)
    mustolah_ulhadeeth_tot = models.IntegerField(blank=True, default = 0)
    cumulative = models.IntegerField(blank=True, default = 0)
    teacher_comment = models.CharField(max_length=200, null=True)
    head_comment = models.CharField(max_length=200, null=True)
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

    def grade_sorf(self):
        if self.sorf_tot < 40:
            return "F - Fail"
        elif self.sorf_tot >= 40 and self.sorf_tot < 45:
            return "E - Weak Pass"
        elif self.sorf_tot >= 45 and self.sorf_tot < 50:
            return "D - Fair"
        elif self.sorf_tot >= 50 and self.sorf_tot < 60:
            return "C - Good"
        elif self.sorf_tot >= 60 and self.sorf_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_uluum_ulquran(self):
        if self.uluum_ulquran_tot < 40:
            return "F - Fail"
        elif self.uluum_ulquran_tot >= 40 and self.uluum_ulquran_tot < 45:
            return "E - Weak Pass"
        elif self.uluum_ulquran_tot >= 45 and self.uluum_ulquran_tot < 50:
            return "D - Fair"
        elif self.uluum_ulquran_tot >= 50 and self.uluum_ulquran_tot < 60:
            return "C - Good"
        elif self.uluum_ulquran_tot >= 60 and self.uluum_ulquran_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_balaagah(self):
        if self.balaagah_tot < 40:
            return "F - Fail"
        elif self.balaagah_tot >= 40 and self.balaagah_tot < 45:
            return "E - Weak Pass"
        elif self.balaagah_tot >= 45 and self.balaagah_tot < 50:
            return "D - Fair"
        elif self.balaagah_tot >= 50 and self.balaagah_tot < 60:
            return "C - Good"
        elif self.balaagah_tot >= 60 and self.balaagah_tot < 70:
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

    def grade_farooid(self):
        if self.farooid_tot < 40:
            return "F - Fail"
        elif self.farooid_tot >= 40 and self.farooid_tot < 45:
            return "E - Weak Pass"
        elif self.farooid_tot >= 45 and self.farooid_tot < 50:
            return "D - Fair"
        elif self.farooid_tot >= 50 and self.farooid_tot < 60:
            return "C - Good"
        elif self.farooid_tot >= 60 and self.farooid_tot < 70:
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

    def grade_taareekh(self):
        if self.taareekh_tot < 40:
            return "F - Fail"
        elif self.taareekh_tot >= 40 and self.taareekh_tot < 45:
            return "E - Weak Pass"
        elif self.taareekh_tot >= 45 and self.taareekh_tot < 50:
            return "D - Fair"
        elif self.taareekh_tot >= 50 and self.taareekh_tot < 60:
            return "C - Good"
        elif self.taareekh_tot >= 60 and self.taareekh_tot < 70:
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

    def grade_aruud(self):
        if self.aruud_tot < 40:
            return "F - Fail"
        elif self.aruud_tot >= 40 and self.aruud_tot < 45:
            return "E - Weak Pass"
        elif self.aruud_tot >= 45 and self.aruud_tot < 50:
            return "D - Fair"
        elif self.aruud_tot >= 50 and self.aruud_tot < 60:
            return "C - Good"
        elif self.aruud_tot >= 60 and self.aruud_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_mantiqoh(self):
        if self.mantiqoh_tot < 40:
            return "F - Fail"
        elif self.mantiqoh_tot >= 40 and self.mantiqoh_tot < 45:
            return "E - Weak Pass"
        elif self.mantiqoh_tot >= 45 and self.mantiqoh_tot < 50:
            return "D - Fair"
        elif self.mantiqoh_tot >= 50 and self.mantiqoh_tot < 60:
            return "C - Good"
        elif self.mantiqoh_tot >= 60 and self.mantiqoh_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_tafseer(self):
        if self.tafseer_tot < 40:
            return "F - Fail"
        elif self.tafseer_tot >= 40 and self.tafseer_tot < 45:
            return "E - Weak Pass"
        elif self.tafseer_tot >= 45 and self.tafseer_tot < 50:
            return "D - Fair"
        elif self.tafseer_tot >= 50 and self.tafseer_tot < 60:
            return "C - Good"
        elif self.tafseer_tot >= 60 and self.tafseer_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_mustolah_ulhadeeth(self):
        if self.mustolah_ulhadeeth_tot < 40:
            return "F - Fail"
        elif self.mustolah_ulhadeeth_tot >= 40 and self.mustolah_ulhadeeth_tot < 45:
            return "E - Weak Pass"
        elif self.mustolah_ulhadeeth_tot >= 45 and self.mustolah_ulhadeeth_tot < 50:
            return "D - Fair"
        elif self.mustolah_ulhadeeth_tot >= 50 and self.mustolah_ulhadeeth_tot < 60:
            return "C - Good"
        elif self.mustolah_ulhadeeth_tot >= 60 and self.mustolah_ulhadeeth_tot < 70:
            return "B - Very Good"
        else:
            return "A - Excellent"

    def grade_general(self):
        if self.cumulative/15 < 40:
            return "F - Fail"
        elif self.cumulative/15 >= 40 and self.mustolah_ulhadeeth_tot < 45:
            return "E - Weak Pass"
        elif self.cumulative/15 >= 45 and self.mustolah_ulhadeeth_tot < 50:
            return "D - Fair"
        elif self.cumulative/15 >= 50 and self.mustolah_ulhadeeth_tot < 60:
            return "C - Good"
        elif self.cumulative/15 >= 60 and self.mustolah_ulhadeeth_tot < 70:
            return "B - Very Good"
        else:
            return "Excellent"

    def cum_perc(self):
        return str(round((self.cumulative/15),4))

# Create your models here.
