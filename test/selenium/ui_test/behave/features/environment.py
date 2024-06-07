# -- FILE: features/environment.py
# USE: behave -D BEHAVE_DEBUG_ON_ERROR %f --no-capture        (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes     (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=no      (to disable debug-on-error)
from libraries.environment_setup import EnvironmentSetup

BEHAVE_DEBUG_ON_ERROR = False

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")

def before_all(context):
    setup_debug_on_error(context.config.userdata)

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import pdb
        pdb.post_mortem(step.exc_traceback)

def before_scenario(context, scenario):
    context.driver = EnvironmentSetup.setUp(context)
    
def after_scenario(context, feature):
    context.driver.quit()
