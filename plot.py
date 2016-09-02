# -*- coding: utf-8 -*-
import csv

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages



# The PDF document
pdf_pages = PdfPages('flat1_variants.pdf')

with open('rooms_a_b.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)

    count = 0
    for row in reader:


        fig = plt.figure(figsize=(20, 20), dpi=100)
        if count == 0:
            count += 1
            continue

        if count == 100:
            break


        print count

        a0 = float(row[0])
        b0 = float(row[1])

        a1 = float(row[2])
        b1 = float(row[3])

        a2 = float(row[4])
        b2 = float(row[5])

        a3 = float(row[6])
        b3 = float(row[7])

        a4 = float(row[8])
        b4 = float(row[9])

        a5 = float(row[10])
        b5 = float(row[11])

        # plt.subplot(3, 3, count)
        plt.title("Total Square: {}".format(sum([a0 * b0, a1 * b1, a2 * b2, a3 * b3, a4 * b4, a5 * b5])))
        # plt.legend(('r_0', 'r_1', 'r_2', 'r_3', 'r_4', 'r_5'), loc=(0.8, 0.1))
        r_0_patch = mpatches.Patch(color='red', label=u'Kitchen: {} x {}'.format(a0, b0))
        r_1_patch = mpatches.Patch(color='blue', label=u'Bathroom: {} x {}'.format(a1, b1))
        r_2_patch = mpatches.Patch(color='green', label=u'Livingroom: {} x {}'.format(a2, b2))
        r_3_patch = mpatches.Patch(color='yellow', label=u'Enterroom: {} x {}'.format(a3, b3))
        r_4_patch = mpatches.Patch(color='black', label=u'Middleroom: {} x {}'.format(a4, b4))
        r_5_patch = mpatches.Patch(color='green', label=u'Wardrobe: {} x {}'.format(a5, b5))
        plt.legend(handles=[r_0_patch, r_1_patch, r_2_patch, r_3_patch, r_4_patch, r_5_patch])

        # plt.annotate('local max', xy=(a3, b3), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05),)

        r0 = plt.plot([0, a0, a0, 0, 0], [0, 0, b0, b0, 0], color='red')
        r1 = plt.plot([0, a1, a1, 0, 0], [b0 + b4, b0 + b4, b0 + b1 + b4, b0 + b1 + b4, b0 + b4], color='blue')
        r2 = plt.plot([-a2, 0, 0, -a2, -a2], [b0, b0, b0 - b2, b0 - b2, b0], color='green')
        r3 = plt.plot([-a2, 0, 0, -a2, -a2], [b0, b0, b0 + b3, b0 + b3, b0], color='yellow')
        r4 = plt.plot([0, a4, a4, 0, 0], [b0, b0, b0 + b4, b0 + b4, b0], color='black')
        r5 = plt.plot([-a2 - a5, -a2, -a2, -a2 - a5, -a2 - a5], [b0, b0, b0 - b5, b0 - b5, b0], color='green')
        # line2 = plt.plot([5, 6, 6, 5, 5], [5, 5, 6, 6, 6])
        # plt.setp([line2], 'color', 'r', 'linewidth', 2.0)
        plt.axis([-10, 10, -10, 10])

        pdf_pages.savefig(fig)

        count += 1

    pdf_pages.close()
