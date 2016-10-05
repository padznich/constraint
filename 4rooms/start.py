import time
import plot_pdf


start = time.time()
import flat_1
plot_pdf.main1()    # CSV output
finish = time.time()

start2 = time.time()
plot_pdf.main()     # PDF output
finish2 = time.time()

print 'THE whole time for CSV output', finish - start
print ""
print 'Additional time for PDF output', finish2 - start2
