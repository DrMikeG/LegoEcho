import time

class StubGPIO:


        triggerTime = 5 # Access through class
        triggerTimerStarted = False

        inOrOutDict = {} # indexed by pin number (int) whether IN or OUT or nothing
        outputDict = {} # # indexed by pin number (int) whether OUTPUT is True or False 

        inputDict = {} # # indexed by pin number (int) whether INPUT is True or False 

        BCM = True
        IN = False
        OUT = True
        HIGH = 1
        LOW = 0

        def __init__(self):
            StubGPIO.triggerTime = 0

        @staticmethod
        def setmode(*args,**kwargs):
            return True

        @staticmethod
        def cleanup(*args,**kwargs):
            StubGPIO.inOrOutDict.clear()
            StubGPIO.outputDict.clear()
            StubGPIO.inputDict.clear()
            return True

        @staticmethod
        def setup(pin, inOrOut):
            #First argument should be int (pin number) 
            #Second argument should be bool (in or out)
            StubGPIO.inOrOutDict[pin] = inOrOut
            return True

        @staticmethod
        def testGetSetup(pin):
            return StubGPIO.inOrOutDict.get(pin)

        @staticmethod    
        def shouldStartTriggerTimer(pin, value):
            should = StubGPIO.triggerTimerStarted == False & \
            StubGPIO.testGetOutput(23) == True & \
            pin == 23 & \
            value == False
            print "should start trigger :"
            print should
            return should

        @staticmethod    
        def startTriggerTimer():
            StubGPIO.triggerTimer = time.time()
            StubGPIO.triggerTimerStarted = True
            StubGPIO.inputDict[24] = False # echo pin is false for duration of timer

        @staticmethod    
        def checkTriggerTimer():
            if StubGPIO.triggerTimerStarted == True:
                if (time.time() - StubGPIO.triggerTimer > 1):
                    StubGPIO.triggerTimerStarted = False
                    StubGPIO.inputDict[24] = True # when timer expires, echo pin goes true

        @staticmethod    
        def output(pin, value):
            StubGPIO.outputDict[pin] = value
            
            if StubGPIO.shouldStartTriggerTimer(pin,value):
                StubGPIO.startTriggerTimer()
                
            return True

        @staticmethod    
        def testGetOutput(pin):
            return StubGPIO.outputDict.get(pin,False)

        @staticmethod
        def input(pin):
            StubGPIO.checkTriggerTimer()

            value = StubGPIO.inputDict.get(pin,False)
            return value
         
        @staticmethod    
        def testSetInput(pin,value):
            StubGPIO.inputDict[pin]=value

   #{"setup", (PyCFunction)py_setup_channel, METH_VARARGS | METH_KEYWORDS, "Set up a GPIO channel or list of channels with a direction and (optional) pull/up down control\nchannel        - either board pin number or BCM number depending on which mode is set.\ndirection      - IN or OUT\n[pull_up_down] - PUD_OFF (default), PUD_UP or PUD_DOWN\n[initial]      - Initial value for an output channel"},
   #{"cleanup", (PyCFunction)py_cleanup, METH_VARARGS | METH_KEYWORDS, "Clean up by resetting all GPIO channels that have been used by this program to INPUT with no pullup/pulldown and no event detection\n[channel] - individual channel or list/tuple of channels to clean up.  Default - clean every channel that has been used."},
   #{"output", py_output_gpio, METH_VARARGS, "Output to a GPIO channel or list of channels\nchannel - either board pin number or BCM number depending on which mode is set.\nvalue   - 0/1 or False/True or LOW/HIGH"},
   #{"input", py_input_gpio, METH_VARARGS, "Input from a GPIO channel.  Returns HIGH=1=True or LOW=0=False\nchannel - either board pin number or BCM number depending on which mode is set."},
   #{"setmode", py_setmode, METH_VARARGS, "Set up numbering mode to use for channels.\nBOARD - Use Raspberry Pi board numbers\nBCM   - Use Broadcom GPIO 00..nn numbers"},
   #{"getmode", py_getmode, METH_VARARGS, "Get numbering mode used for channel numbers.\nReturns BOARD, BCM or None"},
   #{"add_event_detect", (PyCFunction)py_add_event_detect, METH_VARARGS | METH_KEYWORDS, "Enable edge detection events for a particular GPIO channel.\nchannel      - either board pin number or BCM number depending on which mode is set.\nedge         - RISING, FALLING or BOTH\n[callback]   - A callback function for the event (optional)\n[bouncetime] - Switch bounce timeout in ms for callback"},
   #{"remove_event_detect", py_remove_event_detect, METH_VARARGS, "Remove edge detection for a particular GPIO channel\nchannel - either board pin number or BCM number depending on which mode is set."},
   #{"event_detected", py_event_detected, METH_VARARGS, "Returns True if an edge has occurred on a given GPIO.  You need to enable edge detection using add_event_detect() first.\nchannel - either board pin number or BCM number depending on which mode is set."},
   #{"add_event_callback", (PyCFunction)py_add_event_callback, METH_VARARGS | METH_KEYWORDS, "Add a callback for an event already defined using add_event_detect()\nchannel      - either board pin number or BCM number depending on which mode is set.\ncallback     - a callback function"},
   #{"wait_for_edge", (PyCFunction)py_wait_for_edge, METH_VARARGS | METH_KEYWORDS, "Wait for an edge.  Returns the channel number or None on timeout.\nchannel      - either board pin number or BCM number depending on which mode is set.\nedge         - RISING, FALLING or BOTH\n[bouncetime] - time allowed between calls to allow for switchbounce\n[timeout]    - timeout in ms"},
   #{"gpio_function", py_gpio_function, METH_VARARGS, "Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI)\nchannel - either board pin number or BCM number depending on which mode is set."},
   #{"setwarnings", py_setwarnings, METH_VARARGS, "Enable or disable warning messages"},
   #{NULL, NULL, 0, NULL}