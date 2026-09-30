# Sprint 5 Stretch - Radio Control App

This is part of an app that can be used to control an online radio station

Your task is to:
1. Upgrade everything use dataclasses. Use `frozen` where appropriate.
1. Observe how the given `__str__` method works, and add one to the other classes
1. When the `__str__` method is called, have it print the duration in formatted mm:ss rather than just seconds
1. Add a new class of `Person` - you can use your imagination what this includes, but it should have at least a string name
1. Turn the fields for _artists_, _host_, and _guest_ into `Person` classes
1. Make a new class `Podcast` that _extends_ the `TalkShow` class, with an extra string field for _sponsor_
1. Finish implementing the class `Playlist`, and set it to takes a generic, e.g. either `Song` or `TalkShow` or `Podcast`

As you implement, make sure to keep checking with mypy and add your own code at the end to test it works correctly
