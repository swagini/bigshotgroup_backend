import logging
info_logger = logging.getLogger("info_logger")
err_logger = logging.getLogger("error_logger")
print(info_logger,err_logger,"info_logger")

def log_request(request):
    try:
        info_logger.info(request)
        if request.query_params !={}:
            info_logger.info(request.query_parama)
        if request.data !={}:
            info_logger.info(request.data)
        info_logger.info('')
    except Exception as err:
        print(err)



def log_result(result):
    try:
        info_logger.info(result)
        if result.data !={}:
            info_logger.info(result.data)
    except Exception as err:
        print(err)

def log_error(request, http_err):
    try:
        err_logger.error(request)
        if request.query_params !={}:
            err_logger.error(request.query_params)
        if request.data !={}:
            err_logger.error(request.data)
        err_logger.error(http_err)
        err_logger.error('')
    except Exception as err:
        print(err)



