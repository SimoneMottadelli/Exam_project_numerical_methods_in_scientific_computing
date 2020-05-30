# This module contains the function used to display the results obtained with the image processing

import matplotlib.pyplot as plt
import os
import numpy as np
import math as m


# this function shows an interactive window containing two images side by side
def display_images(img1, img2):
    plt.style.use('ggplot')
    plt.figure("Output")
    plt.subplot(1, 2, 1)
    plt.title('Image before compression')
    plt.imshow(img1, cmap=plt.get_cmap('gray'))
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(img2, cmap=plt.get_cmap('gray'))
    plt.title('Image after compression')
    plt.axis('off')
    plt.show()


# This function is used to save on a file the results of the comparison of the dct2 implementations
def save_results_on_file(my_dct2_time, lib_dct2_time, dimension_matrix, step):
    dir = "../results"
    if not os.path.isdir(dir):
        os.makedirs(dir)
    file_name = "%s/output_%d_step_%d.txt" % (dir, dimension_matrix[len(dimension_matrix) - 1], step)
    f = open(file_name, "w")

    f.write("Matrix dimensions: \n")
    f.write("[")
    for i in dimension_matrix[0 : len(dimension_matrix) - 1]:
        f.write(str(i) + ", ")
    f.write(str(dimension_matrix[len(dimension_matrix) - 1]))
    f.write("]\n\n")

    f.write("Execution time of my dct2 implementation: \n")
    f.write("[")
    for i in range(0, len(my_dct2_time) - 1):
        f.write(str(my_dct2_time[i]) + ", ")
    f.write(str(my_dct2_time[len(my_dct2_time) - 1]))
    f.write("]\n\n")

    f.write("Execution time of the dct2 of the library: \n")
    f.write("[")
    for i in range(0, len(lib_dct2_time) - 1):
        f.write(str(lib_dct2_time[i]) + ", ")
    f.write(str(lib_dct2_time[len(lib_dct2_time) - 1]))
    f.write("]")

    f.close()


# This function is used to plot the results of the comparison of the dct2 implementations
#def plot_results(my_dct2_time, lib_dct2_time, dimension_matrix, step):
def plot_results():
    plt.style.use('ggplot') # To improve visualization
    
    # Matrix dimensions: 
    dimension_matrix = [2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 302, 312, 322, 332, 342, 352, 362, 372, 382, 392, 402, 412, 422, 432, 442, 452, 462, 472, 482, 492, 502, 512, 522, 532, 542, 552, 562, 572, 582, 592, 602, 612, 622, 632, 642, 652, 662, 672, 682, 692, 702, 712, 722, 732, 742, 752, 762, 772, 782, 792, 802, 812, 822, 832, 842, 852, 862, 872, 882, 892, 902, 912, 922, 932, 942, 952, 962, 972, 982, 992, 1000]

    # Execution time of my dct2 implementation: 
    my_dct2_time = [0.0, 0.01562666893005371, 0.046894073486328125, 0.15622639656066895, 0.3750011920928955, 0.6562530994415283, 1.2031264305114746, 1.765625238418579, 2.6718642711639404, 3.7969415187835693, 5.34368371963501, 6.765626668930054, 9.031248569488525, 11.328124046325684, 13.828142642974854, 16.578184127807617, 19.812426567077637, 24.09374761581421, 28.81252360343933, 33.859352350234985, 39.031248331069946, 44.98440432548523, 52.578096866607666, 58.75003218650818, 67.40621447563171, 75.15625286102295, 86.24999809265137, 96.01562190055847, 106.43749904632568, 117.92188501358032, 130.28124713897705, 144.71875166893005, 158.06249451637268, 175.42187094688416, 190.37499952316284, 207.6718876361847, 225.57820987701416, 244.17180824279785, 264.42187309265137, 288.6406247615814, 309.82812666893005, 335.562527179718, 358.64062237739563, 385.87499737739563, 411.06257152557373, 440.3906035423279, 469.9687490463257, 501.5937592983246, 529.7968661785126, 572.3125076293945, 604.203117609024, 644.9062492847443, 679.0937404632568, 723.42187666893, 761.9531035423279, 805.4062156677246, 847.9843678474426, 902.5156183242798, 951.9687464237213, 1001.0312626361847, 1049.2187299728394, 1112.3281450271606, 1157.6249661445618, 1216.4999964237213, 1271.0625097751617, 1342.3281326293945, 1402.9843788146973, 1471.4999964237213, 1519.4687485694885, 1597.187509059906, 1670.2968595027924, 1738.6718645095825, 1808.1406843662262, 1902.0781252384186, 1977.421864271164, 2060.8593735694885, 2140.5156247615814, 2227.109370946884, 2305.937493801117, 2392.218756198883, 2486.5000145435333, 2597.2812037467957, 2680.999983549118, 2813.2499799728394, 2885.6406588554382, 3020.21874499321, 3105.8749389648438, 3186.1093435287476, 3301.453110218048, 3439.578133583069, 3524.18749499321, 3660.453122138977, 3782.5781202316284, 3913.0468723773956, 4014.0156247615814, 4143.093723058701, 4274.578169107437, 4426.171894311905, 4568.937476873398, 4722.609375715256, 4817.531243801117]

    # Execution time of the dct2 of the library: 
    lib_dct2_time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.015627622604370117, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01562786102294922, 0.0, 0.015627384185791016, 0.0, 0.015629053115844727, 0.0, 0.015629291534423828, 0.0, 0.0, 0.015614509582519531, 0.03123617172241211, 0.015623807907104492, 0.03124833106994629, 0.0, 0.015626192092895508, 0.015598297119140625, 0.04686594009399414, 0.015627145767211914, 0.0, 0.015666723251342773, 0.015625476837158203, 0.031249284744262695, 0.0781407356262207, 0.015616178512573242, 0.046868085861206055, 0.01563549041748047, 0.015634536743164062, 0.03128933906555176, 0.10938405990600586, 0.017143726348876953, 0.04687333106994629, 0.015626192092895508, 0.03125333786010742, 0.015619993209838867, 0.031260013580322266, 0.01560521125793457, 0.09372806549072266, 0.03125286102294922, 0.04687213897705078, 0.07812786102294922, 0.07810211181640625, 0.01562976837158203, 0.03125190734863281, 0.0781404972076416, 0.015620946884155273, 0.06250429153442383, 0.031189918518066406, 0.04694986343383789, 0.046889305114746094, 0.031235694885253906, 0.09375524520874023, 0.14063191413879395, 0.03126096725463867, 0.031226634979248047, 0.12498593330383301, 0.046875, 0.09374594688415527, 0.031250953674316406, 0.12498259544372559, 0.04687070846557617, 0.1406714916229248, 0.07812833786010742, 0.015630245208740234, 0.17184185981750488, 0.046877384185791016, 0.03125309944152832, 0.15626168251037598, 0.1874988079071045, 0.12502717971801758, 0.04687976837158203, 0.04690814018249512, 0.046864986419677734, 0.18749427795410156, 0.06250143051147461, 0.046875]

    # build first line
    line_my_dct2, = plt.semilogy(dimension_matrix, np.array(my_dct2_time) * 1000)
    line_my_dct2.set_label('my dct2 implementation')
    plt.setp(line_my_dct2, color="b")

    # build second line
    line_lib_dct2, = plt.semilogy(dimension_matrix, np.array(lib_dct2_time) * 1000)
    line_lib_dct2.set_label('dct2 of the library')
    plt.setp(line_lib_dct2, color="r")
    
    # build second line
    line_cubic_time, = plt.semilogy(dimension_matrix, 0.007 * np.array(dimension_matrix) ** 3)
    line_cubic_time.set_label('$O(0.007N^{3})$')
    plt.setp(line_cubic_time, color="g", linestyle="--")
    
    # build second line
    line_log_time, = plt.semilogy(dimension_matrix, (np.array(dimension_matrix) ** 2) * np.array([m.log10(x)*0.0002 for x in dimension_matrix]))
    line_log_time.set_label('$O(0.0002N^{2}log(N))$')
    plt.setp(line_log_time, color="y", linestyle="--")

    # add more graph info
    plt.title("Comparison between the dct2 implementations")
    plt.legend()
    plt.xlabel("Dimension of the matrix (N x N)")
    plt.ylabel("Time in milliseconds (log scale)")

    #dir = "../results/"
    #file_name = "%s/output_%d_step_%d.png" % (dir, dimension_matrix[len(dimension_matrix) - 1], step)
    #if not os.path.isdir(dir):
    #    os.makedirs(dir)

    # plt.savefig("%s/%s" % (dir, file_name))

    # show graph
    plt.show()

if __name__ == "__main__":
    plot_results()