import matplotlib.pyplot as plt
import NumMethods as nm
import numpy as np


def main():
    '''
    Calculates P(x<1|N(0,1)) and P(x>μ+2σ|N(175, 3)) and displays both the GNPDF and CDF
    for each case
    :return:
    '''

    # part 1.  P(x<1|N(0,1))
    mu_a = 0  # mean
    sig_a = 1  # standard deviation
    c_a = 1  # critical value for calculating the probability (i.e., =1 for part 1.)
    p_a = nm.Probability(c_a, (mu_a, sig_a))  # calculate the probability P(x<1|N(0,1))

    # create the illustrative plots for part a
    # step 1: create some data to plot
    x_a = np.linspace(mu_a - 5 * sig_a, mu_a + 5 * sig_a, 500)  # &MISSING CODE HERE&# #create a numpy array using linspace between mu-5*sigma to mu+5*sigma with 500 points
    cdf_a = np.fromiter([nm.CDF(x) for x in x_a], float)  # &MISSING CODE HERE&# #create a numpy array filled with values of CDF for each x in x_a.  I used a list comprehension.
    gnpdf_a = np.fromiter([nm.GNPDF(x) for x in x_a], float)  # &MISSING CODE HERE&# #create a numpy array for f(x) from the GNPDF for each x in x_a.  I used a list comprehension.

    # step 2: build the plots
    plt.subplots(2, 1, sharex=True)  # create two, stacked plots using subplots with sharex=True
    plt.subplot(2, 1, 1)  # set subplot 1 as our focus by using plt.subplot
    plt.plot(x_a, gnpdf_a)  # &MISSING CODE HERE&#)  #plots the gndpf_a vs x_a
    plt.xlim(x_a.min(), x_a.max())  # set the limits for the x axis
    plt.ylim(0, gnpdf_a.max() * 1.1)  # set the limits for the y axis

    # fill in area below GNPDF in range mu_a-5*sig_a to 1
    x_fill = np.linspace(mu_a - 5 * sig_a, c_a, 100)  # &MISSING CODE HERE&# #create a numpy array using linspace for x values from mu-5*sigma to c_a with 100 points
    gnpdf_fill = np.fromiter([nm.GNPDF(x) for x in x_fill], float)  # &MISSING CODE HERE&# #calculate the GNPDF function for each x in x_fill and store in numpy array.  I used a list comprehension.
    ax = plt.gca()  # get the axes for the current plot
    ax.fill_between(x_fill, gnpdf_fill, color='grey', alpha=0.3)  # create the filled region between gnpdf and x axis

    # construct the equation to display on GNPDF using TeX
    text_x = mu_a - 4 * sig_a
    text_y = 0.65 * gnpdf_a.max()
    plt.text(text_x, text_y, r'$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x*\mu}{\sigma})^2}$')  # most of the code is here, but I clipped out the exponent part.
    arrow_x = (c_a - mu_a + 5 * sig_a) * 2 / 3 + (mu_a - 5 * sig_a)  # calculate the x coordinate for where the arrow should point
    arrow_y = (nm.GNPDF(arrow_x, (mu_a, sig_a)) / 2)  # calculate the y coordinate for where the arrow should point
    plt.annotate('P(x<{:0.2f}|N({:0.2f},{:0.2f})={:0.2f}'.format(c_a, mu_a, sig_a, p_a), size=8, xy=(arrow_x, arrow_y), xytext=(1.2 * text_x, 0.6 * text_y), arrowprops=dict(arrowstyle='->', connectionstyle="arc3"))  # draw the arrow with text
    plt.ylabel('f(x)', size=12)  # add a label to the y axis
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=10)  # format tick marks
    ax.xaxis.set_ticklabels([])  # erase x tick labels for the top graph

    # create the CDF plot
    plt.subplot(2, 1, 2)  # select the second plot
    plt.plot(x_a, cdf_a)  # &MISSING CODE HERE&#) #plot cdf_a vs x_a
    plt.ylim(0, 1)  # set limits for the y axis
    plt.ylabel(r'$\Phi(x)=\int_{-\infty}^x f(x)dx$', size=12)  # label the y axis
    plt.xlabel('x')  # add the x label
    plt.plot(c_a, p_a, 'o', markerfacecolor='white', markeredgecolor='red')  # &MISSING CODE HERE&#,'o', markerfacecolor='white', markeredgecolor='red') #put a red circle on the cdf at location c_a, p_a
    ax = plt.gca()  # get the current set of axes
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=10)  # format tick marks
    ax.set_xlim(x_a.min(), x_a.max())  # make sure the x axis has the correct limits

    ax.hlines(p_a, ax.get_xlim()[0], c_a, color='black', linewidth=1)  # draw a horizontal line connecting the y axis to the red circle
    ax.vlines(c_a, 0, p_a, color='black', linewidth=1)  # draw a vertical line connecting the x axis to the red circle
    plt.show()  # show the plot.  Note, the code stops here and waits for the user to close the figure window

    # part 2. P(x > mu + 2 * sigma | N(175, 3))
    mu_b = 175  # mean
    sig_b = 3  # standard deviation
    c_b = mu_b + 2 * sig_b  # critical value for calculating the probability (i.e., =1 for part 1.)
    p_b = nm.Probability(c_b, (mu_b, sig_b), True)  # calculate the probability P(x<1|N(0,1))

    # create the illustrative plots for part a
    # step 1: create some data to plot
    x_b = np.linspace(mu_b - 5 * sig_b, mu_b + 5 * sig_b, 500)  # &MISSING CODE HERE&# #create a numpy array using linspace between mu-5*sigma to mu+5*sigma with 500 points
    cdf_b = np.fromiter([nm.CDF(x, (mu_b, sig_b)) for x in x_b], float)  # &MISSING CODE HERE&# #create a numpy array filled with values of CDF for each x in x_b.  I used a list comprehension.
    gnpdf_b = np.fromiter([nm.GNPDF(x, (mu_b, sig_b)) for x in x_b], float)  # &MISSING CODE HERE&# #create a numpy array for f(x) from the GNPDF for each x in x_b.  I used a list comprehension.

    # step 2: build the plots
    plt.subplots(2, 1, sharex=True)  # create two, stacked plots using subplots with sharex=True
    plt.subplot(2, 1, 1)  # set subplot 1 as our focus by using plt.subplot
    plt.plot(x_b, gnpdf_b)  # &MISSING CODE HERE&#)  #plots the gndpf_a vs x_b
    plt.xlim(x_b.min(), x_b.max())  # set the limits for the x axis
    plt.ylim(0, gnpdf_b.max() * 1.1)  # set the limits for the y axis

    # fill in area below GNPDF in range mu_b-5*sig_b to 1
    x_fill = np.linspace(c_b, mu_b + 5 * sig_b, 100)  # &MISSING CODE HERE&# #create a numpy array using linspace for x values from mu-5*sigma to c_b with 100 points
    gnpdf_fill = np.fromiter([nm.GNPDF(x, (mu_b, sig_b)) for x in x_fill], float)  # &MISSING CODE HERE&# #calculate the GNPDF function for each x in x_fill and store in numpy array.  I used a list comprehension.
    ax = plt.gca()  # get the axes for the current plot
    ax.fill_between(x_fill, gnpdf_fill, color='grey', alpha=0.3)  # create the filled region between gnpdf and x axis

    # construct the equation to display on GNPDF using TeX
    text_x = mu_b - 4 * sig_b
    text_y = 0.65 * gnpdf_b.max()
    plt.text(text_x, text_y, r'$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x*\mu}{\sigma})^2}$')  # most of the code is here, but I clipped out the exponent part.
    arrow_x = 181.5  # calculate the x coordinate for where the arrow should point
    arrow_y = 0.005  # calculate the y coordinate for where the arrow should point
    plt.annotate('P(x<{:0.2f}|N({:0.2f},{:0.2f})={:0.2f}'.format(c_b, mu_b, sig_b, p_b), size=6, xy=(arrow_x, arrow_y), xytext=(180, 0.05), arrowprops=dict(arrowstyle='->', connectionstyle="arc3"))  # draw the arrow with text
    plt.ylabel('f(x)', size=12)  # add a label to the y axis
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=10)  # format tick marks
    ax.xaxis.set_ticklabels([])  # erase x tick labels for the top graph

    # create the CDF plot
    plt.subplot(2, 1, 2)  # select the second plot
    plt.plot(x_b, cdf_b)  # &MISSING CODE HERE&#) #plot cdf_b vs x_b
    plt.ylim(0, 1)  # set limits for the y axis
    plt.ylabel(r'$\Phi(x)=\int_{-\infty}^x f(x)dx$', size=12)  # label the y axis
    plt.xlabel('x')  # add the x label
    plt.plot(c_b, 1 - p_b, 'o', markerfacecolor='white', markeredgecolor='red')  # &MISSING CODE HERE&#,'o', markerfacecolor='white', markeredgecolor='red') #put a red circle on the cdf at location c_b, p_b
    ax = plt.gca()  # get the current set of axes
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=10)  # format tick marks
    ax.set_xlim(x_b.min(), x_b.max())  # make sure the x axis has the correct limits

    ax.hlines(1 - p_b, ax.get_xlim()[0], c_b, color='black', linewidth=1)  # draw a horizontal line connecting the y axis to the red circle
    ax.vlines(c_b, 0, 1 - p_b, color='black', linewidth=1)  # draw a vertical line connecting the x axis to the red circle
    plt.show()  # show the plot.  Note, the code stops here and waits for the user to close the figure window


main()
