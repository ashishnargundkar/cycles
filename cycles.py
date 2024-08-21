import random
import logging


logging.basicConfig(level=logging.DEBUG,
                    format="%(message)s")


MAX_SENSE_OF_DUALITY = 100
MAX_SENSE_OF_ONENESS_AND_LOVE = MAX_SENSE_OF_DUALITY

# Only when you have built a sufficient sense of oneness and dissolved your
# duality will you start your monotonically increasing progress towards God,
# Truth, Self
ONENESS_THRESHOLD_FOR_GODS_LONGING = 30

# Oneness increases every lifetime after crossing a certain threshold. Prior to
# that, for each lifetime, it increases subject to a probability which is a
# reflection of favourable events happening during your lifetime.
ONENESS_INCREMENT_PER_LIFETIME_ESTIMATE = 5

# An estimate of how much karma you're going to accumulate over a lifetime
# Note that karma is easier to accrue than eliminate.
KARMA_INCREMENT_PER_LIFETIME_ESTIMATE = 5

# An estimate of how much karma you burn when you have a sufficiently high
# sense of oneness. Note that karma is easier to accrue than eliminate.
KARMA_DECREMENT_PER_MATERIAL_LIFETIME_ESTIMATE = 2

# You can be on the path to God despite a high karma. Things will fall into
# place, don't worry!.
# KARMA_THRESHOLD_FOR_GODS_LONGING = 300

# You cannot attain enlightenment until your karma is sufficiently lowered
KARMA_THRESHOLD_AFTER_ENLIGHTENMENT = 5

# Number of lifetimes you need to carry out God's work AFTER you attain the
# knowledge of the Self. You will attain moksha when this counter goes to
# 0. Please see comments in live() to understand what is God's work.
LIFETIMES_TO_COMPLETE_GODS_WORK = 5


# You don't have this, to begin with, that's why the whole cycle of births and
# deaths over and over again!
have_knowledge_of_self = False
on_gods_path = False

# Initialised with your evolutionary karma, assumed to be constant for
# everyone
karma = 100
# Should we model it this way instead?
# karma = random.randrange(100 + 1)  # initialised with your evolutionary karma

# Note that sense of duality and sense of oneness are complements of each
# other. They rise and fall together (meaning rise of one results in fall of
# another and vice versa), in equal amounts.
# We could've as well chosen to keep just one of these.
sense_of_duality = MAX_SENSE_OF_DUALITY
sense_of_love_and_oneness = MAX_SENSE_OF_DUALITY - sense_of_duality

# Whether you give up the body for liberation. No birth possible
# (or required) after this.
for_liberation = False

# Happens when there is no reduction in karma and no increase in
# oneness/decrease in sense of duality
lives_wasted = 0

lives_used_for_gods_work = 0

lives_for_lowering_karma_after_adopting_gods_path = 0

total_lives = 0


def be_born():
    global total_lives

    total_lives += 1
    logging.debug("tl: {} | lives_used_for_gods_work: {} | lives_wasted: {}"
                  " | lives_for_lowering_karma_after_adopting_gods_path: {}"
                  " | duality: {} | love_and_oneness: {} | karma: {:.2f}"
                  .format(total_lives,
                          lives_used_for_gods_work,
                          lives_wasted,
                          lives_for_lowering_karma_after_adopting_gods_path,
                          sense_of_duality,
                          sense_of_love_and_oneness,
                          karma))


def live():
    global on_gods_path
    global lives_for_lowering_karma_after_adopting_gods_path

    if not have_knowledge_of_self:
        if sense_of_love_and_oneness < ONENESS_THRESHOLD_FOR_GODS_LONGING:
           # or karma > KARMA_THRESHOLD_FOR_GODS_LONGING:
            # Awaken consciousness by a bit, subject to probability of
            # conducive events occurring in your lifetime.
            # Note that this doesn't depend on karma. You can still be on the
            # path to God despite a high accumulation of karma.
            consider_physical_world_as_ultimate_reality()
        else:
            if not on_gods_path:
                on_gods_path = True
                logging.info("Commenced on the path to God at lifetime"
                             " {}".format(total_lives))

            lives_for_lowering_karma_after_adopting_gods_path += 1

            # This is where you adopt God's path and keep reducing karma and
            # duality in order to attain enlightenment
            # Remember, the more karma you accrue, the more lifetimes it takes
            # to eliminate it sufficiently
            inch_towards_truth(rapidly=True)

        # When you have absolutely obliterated any sense of duality, you attain
        # knowledge of the Self
        if not sense_of_duality:
            attain_knowledge_of_self()
        # else: you'll have to take more birth(s)!
    # else: you're spending the lifetime carrying out God's work, that of
    # spreading awareness of the Self to the masses and getting as many as
    # possible on the path


def inch_towards_truth(rapidly=False):
    global lives_for_lowering_karma_after_adopting_gods_path

    # Awaken consciousness bit by bit without risking wasting an entire
    # lifetime
    awaken_oneness_and_shatter_duality(rapidly)

    if karma > KARMA_THRESHOLD_AFTER_ENLIGHTENMENT:
        # You are consciously/unconsciously eliminating your karma depending
        # upon whether you are on a clear path to enlightenment
        alleviate_karma(rapidly)
    # else: you are consciously holding on to a minimum amount of karma to keep
    # possession of your body for carrying out God's work


def consider_physical_world_as_ultimate_reality():
    global lives_wasted

    # Throw a die to simulate the probability of such events occurring in your
    # lifetime which increase your sense of oneness and love for all kinds of
    # life
    # 0 = favourable (i.e. not caught up in Maya entirely)
    # 1-5 = you'll be so caught up in Maya that your life will be wasted

    entirely_caught_up_in_maya = random.randrange(6)
    if not entirely_caught_up_in_maya:
        logging.debug("Got lucky")

        # You don't have Self realisation yet. By default, inching towards the
        # truth happens without Self realisation (i.e. the
        # "have_knowledge_of_self" parameter is False).
        # You're not on a clear path to God yet. Hence, your karma will reduce
        # only a tiny bit. Also oneness/duality will be affected in small
        # amounts. You have no control yet over the "rapidly" parameter when
        # inching towards the Truth.
        inch_towards_truth()
    else:
        aggravate_karma()
        lives_wasted += 1


def awaken_oneness_and_shatter_duality(rapidly=False):
    global sense_of_duality
    global sense_of_love_and_oneness

    if sense_of_duality:
        if rapidly:
            sense_of_love_and_oneness \
                    += (2 * ONENESS_INCREMENT_PER_LIFETIME_ESTIMATE)
            # To keep the numerical calculations correct (how silly to relegate
            # creation to a mathematical model!), we fix an upper bound
            # Remember again that this upper bound is the same as the upper
            # bound on the sense of duality as both these quantities are
            # duals of each other.
            if sense_of_love_and_oneness > MAX_SENSE_OF_ONENESS_AND_LOVE:
                sense_of_love_and_oneness = MAX_SENSE_OF_ONENESS_AND_LOVE

            sense_of_duality -= (2 * ONENESS_INCREMENT_PER_LIFETIME_ESTIMATE)

            # To keep the numerical calculations correct (how silly to relegate
            # creation to a mathematical model!), we fix a lower bound
            if sense_of_duality < 0:
                sense_of_duality = 0
        else:
            sense_of_love_and_oneness \
                += ONENESS_INCREMENT_PER_LIFETIME_ESTIMATE
            sense_of_duality -= ONENESS_INCREMENT_PER_LIFETIME_ESTIMATE


def alleviate_karma(exponentially=False):
    global karma

    if exponentially:
        # When you are on a clear path to God (i.e. realisation of Self),
        # you are in a hurry to burn your karma. You make every effort to
        # get rid of you karma as fast as you can. With every lifetime, you
        # get better and better, and faster and faster at burning karma.
        karma_reduction_coeff = 2 * (1 + (sense_of_love_and_oneness / 100))
        karma -= (karma_reduction_coeff
                  * 5)

        if karma < KARMA_THRESHOLD_AFTER_ENLIGHTENMENT:
            # We are not letting you go beyond the minimum karma lest you
            # accidentally slip out of your body without attaining knowledge of
            # the Self! The physical equivalent of this is to place metal on
            # strategic parts of the body to prevent its accidental
            # renunciation.
            karma = KARMA_THRESHOLD_AFTER_ENLIGHTENMENT
    else:
        karma -= KARMA_DECREMENT_PER_MATERIAL_LIFETIME_ESTIMATE


def aggravate_karma():
    global karma

    karma += KARMA_INCREMENT_PER_LIFETIME_ESTIMATE


def give_up_body(for_liberation=False, consciously=False):
    global karma

    if for_liberation:
        # You make all your karma vanish into nothingness
        karma = 0


def attain_knowledge_of_self():
    global karma
    global total_lives
    global have_knowledge_of_self

    have_knowledge_of_self = True

    # Once you become a master of the Self, you can manipulate karma like a
    # child masterfully plays with its toys. You are immediately in a
    # position to shed excess karma just as easily as you would shed clothes.
    # However, because you still have to carry out God's work in the physical
    # realm, you still need to hold on to some bit of karma - which is the
    # cement between the Self and the body that the creator gave you.
    karma = KARMA_THRESHOLD_AFTER_ENLIGHTENMENT

    logging.info("Attained knowledge of the Self at lifetime"
                 " {}".format(total_lives))
    logging.info("Wasted {} lives in realising the Truth".format(lives_wasted))
    logging.info("Took {} lives to sufficiently get rid of"
                 " karma for realising the Self".format(
                     lives_for_lowering_karma_after_adopting_gods_path))


def merge_with_creation():
    # Everything except divine bliss ceases to exist
    pass


# The simple cycle of births and deaths.
# Death is not the tragedy, too many births is the real tragedy!
while karma > 0:
    be_born()
    live()

    if not have_knowledge_of_self:
        # When you don't have knowledge of the Self, you have no control over
        # the "consciously" parameter when giving up your body. Nature will
        # forcefully take it away from you. Similarly, you have no control over
        # the "for_liberation" parameter at this stage.
        # Remember that defaults are False.
        give_up_body()
    else:
        lives_used_for_gods_work += 1

        if lives_used_for_gods_work == LIFETIMES_TO_COMPLETE_GODS_WORK:
            for_liberation = True

        give_up_body(for_liberation, consciously=True)

logging.info("Took {} lifetimes to merge with the creator!"
             .format(total_lives))
merge_with_creation()
