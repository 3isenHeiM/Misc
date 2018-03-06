#!/usr/bin/env pytho

import logging
from logging import handlers
from optparse import OptionParser

LOGFILE = "/var/log/files.log"

# ---- Configure logging correctly -------------------------------------------
def configureLogging():
    ## VARIABLES
    format_entry = '%(asctime)s.%(msecs)03d [%(levelname)-8s] %(message)s'
    format_date = '%Y-%m-%d %H:%M:%S'

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(format_entry, format_date)

    # Output the logs if asked (DEBUG mode)
    if options.console :
        # Logging to sys.stderr
        consolehandler = logging.StreamHandler(sys.stdout)
        #consolehandler.setLevel(log_lvl)
        consolehandler.setFormatter(formatter)
        logger.addHandler(consolehandler)

    try :
        # Log file rotation is assured by logrotate
        filehandler = logging.FileHandler(options.logfile)

        # We can set here different log formats for the stderr output !
        #filehandler.setLevel(0)
        # use the same format as the file
        filehandler.setFormatter(formatter)
        # add the handler to the root logger
        logger.addHandler(filehandler)

    except Exception as e :
        if hasattr(e, 'message') :
            logging.fatal("Exception caught : %s" %e)#.message)
        else :
            logging.fatal("Exception %s caught" %e)

    logging.info("*** Begin of %s ***" %sys.argv[0] )
    logging.info("Logging correctly configured.")

# ---- Parse the command-line arguments and set the options accordingly
def create_options():
  desc = '%s (%s). Version %s.' % (about_info["name"],
                                  about_info["product_number"],
                                  about_info["version"])
  parser = OptionParser(description = desc)

## MANAGEMENT OPTIONS  
  parser.add_option('--console',
    dest='console', action='store_true', default=False,
    help = "If logging to console is wanted. Debug only")

  parser.add_option("-o", "--output-path", type = "string",
    dest = "logfile", action = "store", default = LOGFILE,
    help = "Logfile to write into. The Directory must have " \
            "been created in advance. " \
           "Default is '%s'" % LOGFILE)

  (options, args) = parser.parse_args()
  return [options, args, parser]



if __name__ == "__main__" :

        (options, args,parser) = create_options()
        configureLogging()

    ################################################################################
    #
    #                               m a i n l i n e
    #
    ################################################################################


  
        logging.info("*** End of program %s." %sys.argv[0])
        exit(0)

#EOF

