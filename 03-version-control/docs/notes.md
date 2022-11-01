pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 748 | location 10727-10729 | Added on Wednesday, 19 October 2022 15:41:07

The first thing that we must consider when creating code files is how to keep them in a location where they can be retrieved and used by us and others.
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 748 | location 10730-10732 | Added on Wednesday, 19 October 2022 15:41:33

we would like a way to track these changes and keep the latest ones available for download. If the new changes do not work, we would like ways to roll back the changes and reflect the differences in the history of the file.
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 749 | location 10732-10734 | Added on Wednesday, 19 October 2022 15:42:15

The second question is the collaboration process between our team members. If we work with other network engineers, we will most likely need to work collectively on the files.
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 749 | location 10735-10735 | Added on Wednesday, 19 October 2022 15:42:32

any kind of text-based file should be tracked with multiple inputs that everybody in the team should be able to see.
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 749 | location 10736-10736 | Added on Wednesday, 19 October 2022 15:42:40

The third question is accountability.
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 757 | location 10858-10859 | Added on Thursday, 20 October 2022 07:41:42

Once git is installed, we need to configure a few things so our commit messages can contain the correct information:
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 759 | location 10874-10874 | Added on Thursday, 20 October 2022 07:42:46

gitignore
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 767 | location 10999-11000 | Added on Thursday, 20 October 2022 07:47:50

We can show the history of the commits with git log
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 767 | location 11013-11014 | Added on Thursday, 20 October 2022 07:48:58

We can also show more details about the change using the commit ID:
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 768 | location 11027-11030 | Added on Thursday, 20 October 2022 07:51:52

If you need to revert the changes you have made, you can choose between revert and reset. revert changes all the file for a specific commit back to its state before the commit:
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 769 | location 11037-11039 | Added on Thursday, 20 October 2022 07:52:14

The revert command will keep the commit you reverted and make a new commit. You will be able to see all the changes up to that point, including the revert:
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 770 | location 11050-11052 | Added on Thursday, 20 October 2022 07:52:29

The reset option will reset the status of your repository to an older version and discard all the changes in between:
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 771 | location 11073-11076 | Added on Thursday, 20 October 2022 07:53:45

Git branch A branch in git is a line of development within a repository. Git allows many branches and thus different lines of development within a repository.
==========
pastering Python Networking, Third Edition (Eric Chou)
- Your Highlight on page 772 | location 11077-11079 | Added on Thursday, 20 October 2022 07:54:24

In our example, let us create a branch that represents development, appropriately named the dev branch:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 595-597 | Added on Sunday, 23 October 2022 00:26:46

--global option, because then Git will always use that information for anything you do on that system. If you want to override this with a different name or email address for specific projects, you can run the command without the --global option when you’re in that project.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 633-636 | Added on Sunday, 23 October 2022 00:30:34

If you ever need help while using Git, there are three equivalent ways to get the comprehensive manual page (manpage) help for any of the Git commands: $ git help <verb> $ git <verb> --help $ man git-<verb>
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 684-684 | Added on Sunday, 23 October 2022 00:37:27

At this point,
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 684-684 | Added on Sunday, 23 October 2022 00:37:34

At this point, nothing in your project is tracked yet.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 694-697 | Added on Sunday, 23 October 2022 00:38:43

git clone. If you’re familiar with other VCSs such as Subversion, you’ll notice that the command is "clone" and not "checkout". This is an important distinction — instead of getting just a working copy, Git receives a full copy of nearly all data that the server has. Every version of every file for the history of the project is pulled down by default when you run git clone.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 771-772 | Added on Sunday, 23 October 2022 11:10:34

git add is a multipurpose command — you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 796-799 | Added on Sunday, 23 October 2022 11:12:47

git status output is pretty comprehensive, it’s also quite wordy. Git also has a short status flag so you can see your changes in a more compact way. If you run git status -s or git status --short you get a far more simplified output from the command:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 817-820 | Added on Sunday, 23 October 2022 11:16:38

The rules for the patterns you can put in the .gitignore file are as follows: Blank lines or lines starting with # are ignored. Standard glob patterns work, and will be applied recursively throughout the entire working tree. You can start patterns with
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 820-822 | Added on Sunday, 23 October 2022 11:16:51

You can end patterns with a forward slash (/) to specify a directory. You can negate a pattern by starting it with an exclamation point (!).
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 817-820 | Added on Sunday, 23 October 2022 11:16:57

The rules for the patterns you can put in the .gitignore file are as follows: Blank lines or lines starting with # are ignored. Standard glob patterns work, and will be applied recursively throughout the entire working tree. You can start patterns with a forward slash (/) to avoid recursivity.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 822-826 | Added on Sunday, 23 October 2022 11:18:12

Glob patterns are like simplified regular expressions that shells use. An asterisk (*) matches zero or more characters; [abc] matches any character inside the brackets (in this case a, b, or c); a question mark (?) matches a single character; and brackets enclosing characters separated by a hyphen ([0-9]) matches any character between them (in this case 0 through 9).
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 833-834 | Added on Sunday, 23 October 2022 11:19:27

GitHub maintains a fairly comprehensive list of good .gitignore file examples for dozens of projects and languages
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 844-847 | Added on Sunday, 23 October 2022 11:20:38

We’ll cover git diff in more detail later, but you’ll probably use it most often to answer these two questions: What have you changed but not yet staged? And what have you staged that you are about to commit? Although git status answers those questions very generally by listing the file names, git diff shows you the exact lines added and removed — the patch, as it were.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 863-864 | Added on Sunday, 23 October 2022 11:22:22

If you want to see what you’ve staged that will go into your next commit, you can use git diff --staged. This command compares your staged changes to your last commit:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 890-893 | Added on Sunday, 23 October 2022 11:24:56

Git Diff in an External Tool We will continue to use the git diff command in various ways throughout the rest of the book. There is another way to look at these diffs if you prefer a graphical or external diff viewing program instead. If you run git difftool instead of git diff, you can view any of these diffs in software like emerge, vimdiff
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 899-901 | Added on Sunday, 23 October 2022 11:25:27

The simplest way to commit is to type git commit: $ git commit
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 914-915 | Added on Sunday, 23 October 2022 11:27:20

When you exit the editor, Git creates your commit with that commit message (with the comments and diff stripped out).
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 915-916 | Added on Sunday, 23 October 2022 11:27:44

Alternatively, you can type your commit message inline with the commit command by specifying it after a -m flag,
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 922-923 | Added on Sunday, 23 October 2022 11:29:10

Every time you perform a commit, you’re recording a snapshot
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 924-926 | Added on Sunday, 23 October 2022 11:30:50

Skipping the Staging Area Although it can be amazingly useful for crafting commits exactly how you want them, the staging area is sometimes a bit more complex than you need in your workflow. If you want to skip the staging area, Git provides a simple shortcut.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 926-928 | Added on Sunday, 23 October 2022 11:31:03

Adding the -a option to the git commit command makes Git automatically stage every file that is already tracked before doing the commit, letting you skip the git add part:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 935-936 | Added on Sunday, 23 October 2022 11:31:26

sometimes this flag will cause you to include unwanted changes.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 937-939 | Added on Sunday, 23 October 2022 11:31:47

To remove a file from Git, you have to remove it from your tracked files (more accurately, remove it from your staging area) and then commit. The git rm command does that, and also removes the file from your working directory so you don’t see it as an untracked file the next time around.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 949-951 | Added on Sunday, 23 October 2022 11:33:13

If you modified the file or had already added it to the staging area, you must force the removal with the -f option.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 952-955 | Added on Sunday, 23 October 2022 11:34:11

Another useful thing you may want to do is to keep the file in your working tree but remove it from your staging area. In other words, you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your .gitignore file and accidentally staged it, like a large log file or a bunch of .a compiled files. To do this, use the
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 952-955 | Added on Sunday, 23 October 2022 11:34:16

Another useful thing you may want to do is to keep the file in your working tree but remove it from your staging area. In other words, you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your .gitignore file and accidentally staged it, like a large log file or a bunch of .a
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 952-955 | Added on Sunday, 23 October 2022 11:34:22

Another useful thing you may want to do is to keep the file in your working tree but remove it from your staging area. In other words, you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your .gitignore file and accidentally staged it, like a large log file or a bunch of .a
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 952-955 | Added on Sunday, 23 October 2022 11:34:42

Another useful thing you may want to do is to keep the file in your working tree but remove it from your staging area. In other words, you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your .gitignore file and accidentally staged it, like a large log file or a bunch of .a compiled files. To do this, use the --cached
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 952-956 | Added on Sunday, 23 October 2022 11:35:08

Another useful thing you may want to do is to keep the file in your working tree but remove it from your staging area. In other words, you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your .gitignore file and accidentally staged it, like a large log file or a bunch of .a compiled files. To do this, use the --cached option: $ git rm --cached README
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 965-966 | Added on Sunday, 23 October 2022 11:35:55

poving Files Unlike many other VCSs, Git doesn’t explicitly track file movement.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 967-971 | Added on Sunday, 23 October 2022 11:36:27

Thus it’s a bit confusing that Git has a mv command. If you want to rename a file in Git, you can run something like: $ git mv file_from file_to and it works fine. In fact, if you run something like this and look at the status, you’ll see that Git considers it a renamed file:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 974-978 | Added on Sunday, 23 October 2022 11:36:59

However, this is equivalent to running something like this: $ mv README.md README $ git rm README.md $ git add README Git figures out that it’s a rename implicitly, so it doesn’t matter if you rename a file that way or with the mv command. The only real difference is that git mv is one command instead of three —
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 981-981 | Added on Sunday, 23 October 2022 11:37:29

Viewing the Commit History
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 996-998 | Added on Sunday, 23 October 2022 11:38:35

-p or --patch, which shows the difference (the patch output) introduced in each commit. You can also limit the number of log entries displayed, such as using -2 to show only the last two entries.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1012-1012 | Added on Sunday, 23 October 2022 11:39:13

example, if you want to see some abbreviated stats for each commit, you can use the --stat option:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1012-1012 | Added on Sunday, 23 October 2022 11:39:20

example, if you want to see some abbreviated stats for each commit, you can use the --stat option:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1012-1012 | Added on Sunday, 23 October 2022 11:39:28

if you want to see some abbreviated stats for each commit, you can use the --stat option:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1023-1027 | Added on Sunday, 23 October 2022 11:40:44

--pretty. This option changes the log output to formats other than the default. A few prebuilt option values are available for you to use. The oneline value for this option prints each commit on a single line, which is useful if you’re looking at a lot of commits. In addition, the short, full, and fuller values show the output in roughly the same format
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1023-1027 | Added on Sunday, 23 October 2022 11:40:48

--pretty. This option changes the log output to formats other than the default. A few prebuilt option values are available for you to use. The oneline value for this option prints each commit on a single line, which is useful if you’re looking at a lot of commits. In addition, the short, full, and fuller values show the output in roughly the same format but with less or more information,
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1030-1031 | Added on Sunday, 23 October 2022 11:41:14

The most interesting option value is format, which allows you to specify your own log output format.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1056-1058 | Added on Sunday, 23 October 2022 11:42:12

The oneline and format option values are particularly useful with another log option called --graph. This option adds a nice little ASCII graph showing your branch and merge history:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1063-1063 | Added on Sunday, 23 October 2022 11:42:32

This type of output will become more interesting as we go through branching
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1083-1084 | Added on Sunday, 23 October 2022 11:49:54

Limiting Log Output In addition to output-formatting options, git log takes a number of useful limiting options; that is, options that let you show only a subset of commits
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1134-1135 | Added on Sunday, 23 October 2022 12:15:59

you may lose some work if you do it wrong.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1142-1144 | Added on Sunday, 23 October 2022 12:19:24

As an example, if you commit and then realize you forgot to stage the changes in a file you wanted to add to this commit, you can do something like this: $ git commit -m 'Initial commit' $ git add forgotten_file $ git commit --amend
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1148-1150 | Added on Sunday, 23 October 2022 12:22:18

obvious value to amending commits is to make minor improvements to your last commit, without cluttering your repository history with commit messages of the form, â€œOops, forgot to add
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1151-1151 | Added on Sunday, 23 October 2022 12:22:36

Only amend commits that are still local and have not been pushed somewhere.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1186-1188 | Added on Sunday, 23 October 2022 15:02:59

It’s important to understand that git checkout -- <file> is a dangerous command. Any local changes you made to that file are gone
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1241-1243 | Added on Sunday, 23 October 2022 15:06:38

To see which remote servers you have configured, you can run the git remote command. It lists the shortnames of each remote handle you’ve specified. If you’ve cloned your repository, you should at least see origin — that is the default name Git
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1241-1244 | Added on Sunday, 23 October 2022 15:07:34

To see which remote servers you have configured, you can run the git remote command. It lists the shortnames of each remote handle you’ve specified. If you’ve cloned your repository, you should at least see origin — that is the default name Git gives to the server you cloned from:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1248-1249 | Added on Sunday, 23 October 2022 15:08:13

-v, which shows you the URLs that Git has stored for the shortname to be used when reading and writing to that remote:
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1286-1288 | Added on Sunday, 23 October 2022 15:33:48

If your current branch is set up to track a remote branch (see the next section and Git Branching for more information), you can use the git pull command to automatically fetch and then merge that remote branch into your current branch.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1289-1290 | Added on Sunday, 23 October 2022 15:34:15

by default, the git clone command automatically sets up your local master branch to track the remote master branch (or whatever the default branch
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1291-1292 | Added on Sunday, 23 October 2022 15:34:30

git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you’re currently working on.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1350-1352 | Added on Sunday, 23 October 2022 16:09:12

Like most VCSs, Git has the ability to tag specific points in a repository’s history as being important. Typically, people use this functionality to mark release points (v1.0, v2.0 and so on).
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1358-1358 | Added on Sunday, 23 October 2022 16:11:21

search for tags that match a particular pattern.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1427-1428 | Added on Sunday, 23 October 2022 16:30:44

To delete a tag on your local repository, you can use git tag -d <tagname>.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1430-1431 | Added on Sunday, 23 October 2022 16:30:58

There are two common variations for deleting a tag from a remote server.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1431-1435 | Added on Sunday, 23 October 2022 16:31:51

first variation is git push <remote> :refs/tags/<tagname>: $ git push origin :refs/tags/v1.4-lw To /git@github.com:schacon/simplegit.git - [deleted] v1.4-lw The way to interpret the above is to read it as the null value before the colon is being pushed to the remote tag name, effectively deleting it.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1431-1435 | Added on Sunday, 23 October 2022 16:31:58

The first variation is git push <remote> :refs/tags/<tagname>: $ git push origin :refs/tags/v1.4-lw To /git@github.com:schacon/simplegit.git - [deleted] v1.4-lw The way to interpret the above is to read it as the null value before the colon is being pushed to the remote tag name, effectively deleting it.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1435-1437 | Added on Sunday, 23 October 2022 16:32:16

The second (and more intuitive) way to delete a remote tag is with: $ git push origin --delete <tagname>
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1457-1461 | Added on Sunday, 23 October 2022 16:34:13

Git doesn’t automatically infer your command if you type it in partially. If you don’t want to type the entire text of each of the Git commands, you can easily set up an alias for each command using git config. Here are a couple of examples you may want to set up: $ git config --global alias.co checkout $ git config --global alias.br branch $ git config --global alias.ci commit $ git config --global alias.st status
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1475-1476 | Added on Sunday, 23 October 2022 16:35:21

Git simply replaces the new command with whatever you alias it for. However, maybe you want to run an external command, rather than a Git subcommand. In that case, you start the command with a ! character.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1492-1493 | Added on Sunday, 23 October 2022 16:36:43

To really understand the way Git does branching, we need to take a step back and examine how Git stores its data.
==========
Pro Git - Scott Chacon & Ben Straub (Scott Chacon)
- Your Highlight at location 1496-1498 | Added on Sunday, 23 October 2022 16:37:37

commits that directly came before this commit (its parent or parents): zero parents for the initial commit, one parent for a normal commit, and multiple parents for a commit that results from a merge of two or more branches.
==========
