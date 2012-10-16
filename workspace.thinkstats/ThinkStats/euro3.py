"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

"""This file contains a partial solution to a problem from
MacKay, "Information Theory, Inference, and Learning Algorithms."

    Exercise 3.15 (page 50): A statistical statement appeared in
    "The Guardian" on Friday January 4, 2002:

        When spun on edge 250 times, a Belgian one-euro coin came
        up heads 140 times and tails 110.  'It looks very suspicious
        to me,' said Barry Blight, a statistics lecturer at the London
        School of Economics.  'If the coin were unbiased, the chance of
        getting a result as extreme as that would be less than 7%.'

MacKay asks, "But do these data give evidence that the coin is biased
rather than fair?"

"""

import thinkbayes
import myplot


class Euro(thinkbayes.Suite):

    def Likelihood(self, hypo, data):
        """Computes the likelihood of the data under the hypothesis.

        hypo: integer value of x, the probability of heads (0-100)
        data: tuple of (number of heads, number of tails)
        """
        x = hypo / 100.0
        heads, tails = data
        like = x**heads * (1-x)**tails
        return like



def Main():
    data = 140, 110

    suite1 = Euro()
    likelihoodF = suite1.Likelihood(50, data)
    print 'p(D|F)', likelihoodF

    actual_percent = 100.0 * 140 / 250
    likelihood = suite1.Likelihood(actual_percent, data)
    print 'p(D|B_cheat)', likelihood
    print 'p(D|B_cheat) / p(D|F)', likelihood / likelihoodF

    suite_uniform = Euro(xrange(0, 101))
    likelihood = suite_uniform.Update(data)
    print 'p(D|B_uniform)', likelihood

    


if __name__ == '__main__':
    Main()
