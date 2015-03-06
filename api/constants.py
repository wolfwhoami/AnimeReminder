#codung: utf-8
SUBSCRIPTION_UNWATCHED = 0
SUBSCRIPTION_WATCHING = 1
SUBSCRIPTION_WATCHED = 2
SUBSCRIPTION_FORGONE = 3
SUBSCRIPTION_STATUS = (
    (SUBSCRIPTION_UNWATCHED, 'unwatch'),
    (SUBSCRIPTION_WATCHING, 'watching'),
    (SUBSCRIPTION_WATCHED, 'watched'),
    (SUBSCRIPTION_FORGONE, 'forgone'),
)