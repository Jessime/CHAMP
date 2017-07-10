import champ
import numpy as np
import matplotlib.pyplot as plt
import pdb,sys,traceback,logging

DESCRIPTION = ""
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"

def main():
    logging.basicConfig(format=LOG_FORMAT,
                        level=LOG_LEVEL)
    logging.info("Command: %s", " ".join(sys.argv))
    #create random planes
    test_hs=[]
    np.random.seed(0)

    # print test_hs
    # print test_int_dict
    test_hs_arry=champ.get_random_halfspaces(50)
    print test_hs_arry.shape
    print test_hs_arry
    test_hs=champ.create_halfspaces_from_array(test_hs_arry)
    print len(test_hs)

    logging.info("Number of Initial Partitions: %d" %(len(test_hs)) )
    ind_2_doms=champ.get_intersection(test_hs)
    logging.info("Number of Admissible Partitions: %d" %(len(ind_2_doms.keys())))


    #plot domain by domain
    # for i,dom in ind_2_doms.items():
    #     plt.close()
    #     champ.plot_2d_domains(dict([(i,dom)]))
    #     plt.show()
    plt.close()
    ax=champ.plot_2d_domains(ind_2_doms)
    # print ind_2_doms
    plt.show()
    return 1

def pydebug(type, value, tb):
    logging.error("Error type:" + str(type) + ": " + str(value))
    traceback.print_tb(tb)
    pdb.pm()


if __name__ == '__main__':
    sys.excepthook = pydebug
    sys.exit(main())
