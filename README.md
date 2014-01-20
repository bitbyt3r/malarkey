malarkey
========

A new take on a configuration management system for Linux

This project started as I worked with other CMS's and got fed up with the approach.
I don't know if I have actually solved anything, but I think my method makes some 
sense, and I am willing to see where this goes.

Basically, the idea here is to create a CMS that works with any language. You should
be able to write configuration in whatever language you like. Basically, this is
more of a framework and less of a system than the classic CMS. I aim to provide the
following things:
 - A standardized key-value store that supports profiles, inheritance, and several
   useful datatypes.
 - A common interface for scripts to retrieve their configuration
 - Triggers to fire off scripts as necessary
 - Revision control on everything, files, database, and scripts
 - A global repository for people to upload useful scripts, and a simple method to
   find and retrieve them
 - A useful standard library
 - Monitoring of configuration deployment

I plan to write libraries for several popular languages to help them interact
directly with the database, as well as a simple web interface for monitoring
and editing configuration.

What problems does this solve?
 - One main issue with some systems is that they require their own language.
   I think it is better to start off with already used languages complete with
   their extensive libraries and brain share. I also aim to allow any language
   to be used with this system. Use what you already know.
 - Integrated revision control means you can branch and pull the branch on your
   test environment, then merge back into production later, or revert changes.
   Unlike other systems, nodes are aware of the revision control, you can do 
   some neat things: make a change on a node, then push it to all the others
   without talking directly to the central server, you can run testing on a
   different branch than production, whatever.
 - Basing the configuration in git means that it is distributed by default.
   If your server dies, you can get your full history from any node.
