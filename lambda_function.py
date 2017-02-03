"""
Copyright Anjishnu Kumar 2015
"""

from ask import alexa
import random

excuse_list = ["My dog died","I'm dead","I ate too much",
                "I have some scheduled snuggle time",
                "Uggh, work was so draining","I have to practice yoga",
                "There is too much TV to watch",
                "I have a hot date with a piece of pizza",
                "Um, internet? Maybe youve heard of it?",
                "If I don't do laundry I will literally have to leave the house naked tomorrow",
                "I'm building a fort"]

def excuse():
    pass

def lambda_handler(request_obj, context=None):
    '''
    This is the main function to enter to enter into this code.
    If you are hosting this code on AWS Lambda, this should be the entry point.
    Otherwise your server can hit this code as long as you remember that the
    input 'request_obj' is JSON request converted into a nested python object.
    '''

    metadata = {'user_name' : 'SomeRandomDude'} # add your own metadata to the request using key value pairs

    ''' inject user relevant metadata into the request if you want to, here.
    e.g. Something like :
    ... metadata = {'user_name' : some_database.query_user_name(request.get_user_id())}

    Then in the handler function you can do something like -
    ... return alexa.create_response('Hello there {}!'.format(request.metadata['user_name']))
    '''
    return alexa.route_request(request_obj, metadata)


@alexa.default_handler()
def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request """
    return alexa.create_response(message="Goodbye!",end_session=True)


@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="Hello and welcome to Excuse Me! Ask me for an excuse.")


@alexa.request_handler("SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Thank you and good luck!",
            end_session=True)

@alexa.intent_handler("AMAZON.NoIntent")
def no_intent_handler(request):
    return alexa.create_response(message="Okay, goodbye.", end_session=True)

    
@alexa.intent_handler('GetExcuseIntent')
def get_excuse_intent_handler(request):
    """
    You can insert arbitrary business logic code here
    """
    excuse = random.choice(excuse_list)

    card = alexa.create_card(title="ExcuseMe", subtitle=None,
                content="I came up with the excuse: {}.".format(excuse))

    return alexa.create_response("A great excuse would be... {}".format(excuse),
                end_session=True, card_obj=card)
    # # Get variables like userId, slots, intent name etc from the 'Request' object
    # ingredient = request.slots["Ingredient"]
    #
    # if ingredient == None:
    #     return alexa.create_response("Could not find an ingredient!")

@alexa.intent_handler("AMAZON.HelpIntent")
def help_intent_handler(request):

    card = alexa.create_card(title="Here's some help",
            content="Simply say one of the following:\nAlexa, ask ExcuseMe! for and excuse.\nAlexa, ask ExcuseMe! to find an excuse for me.")

    return alexa.create_response(message="Simply ask for an excuse by saying, Alexa, ask Excuse Me for and excuse. Or check the Alexa app for more options", end_session=True, card_obj=card)
# @alexa.intent_handler('NextRecipeIntent')
# def next_recipe_intent_handler(request):
#     """
#     You can insert arbitrary business logic code here
#     """
#     return alexa.create_response(message="Getting Next Recipe ... 123")
