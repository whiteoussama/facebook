import os, sys, time


# Set Colors ######

N = '\033[0m'

W = '\033[1;37m'

B = '\033[1;34m'

R = '\033[1;31m'

G = '\033[1;32m'

Y = '\033[1;33m'

C = '\033[1;36m'

##################


# Restart ####################

def restart_program():

   python = sys.executable

   os.execl(python, python, * sys.argv)

   curdir = os.getcwd()

##############################


os.system("clear")

print "%s ____ ___ %s" % (W, N)

print "%s / __// o.) %s.__ %s . . . %s" % (W, B, R, N)

print "%s / _/ / o \ %s[ __._._ . .[_) %s|_| _. _.;_/ %s" % (W, B, R, N)

print "%s /_/ /___,' %s[_./[ (_)(_|[_)%s | |(_](_.| \ %s" % (W, B, R, N)

print " %s============================%s|%s======================%s " % (C, B, C, N)

print " %sFB%s gang%s Hack %s12-09-2018%s (0:55)%s" % (W, B, R, C, Y, N)

print " %sDevelop by: %sOussama Arkoubi%s$$$%s Mr.gang%s" % (W, R, W, Y, N)
print "                      %sAnd %sMaNiSh%s" % (W, R, N)

print " %sCode: %sPython%s" % (W, C, N)

print " %sFB: %shttps://https://m.facebook.com/betsy.feliz%s" % (W, B, N)

print " %sThis purpose is for educational only%s" % (C, N)

print " %sI take no responsibilities for the use of this%s" % (Y, N)

print " %sprogram%s" % (Y, N)

print "%s ===================================================%s" % (C, N)

print

print " %sLanguage/Bahasa:%s" % (W, N)

print

print "%s (%s01%s)%s -- %sIndonesia%s" % (B, C, B, Y, W, N)

print "%s (%s02%s)%s -- %sEnglish%s" % (B, C, B, Y, W, N)

print "%s (%s03%s)%s -- %sTetum%s" % (B, C, B, Y, W, N)

print

bahasa = raw_input("%s[%s*%s] %sPilih/Choose/Hili:%s " % (C, Y, C, W, B))


try:

        file = open("link.txt", 'w')

except(IOError):

        print "ERROR"

        sys.exit()


if bahasa.strip() in "01 1".split():

  print " %s[%s Indonesia%s ]%s" % (R, W, R, N)
  print

  tahap1 = raw_input("%s1%s)%s Pertama cari grup di%s facebook%s yang ingin kamu%s hack%s...%s[%sEnter%s]%s" % (Y, C, W$

  print "%s--------------------%s" % (R, N)

  tahap2 = raw_input("%s2%s)%s Setelah itu
