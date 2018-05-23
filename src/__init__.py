# https://stackoverflow.com/questions/448271/what-is-init-py-for
# Q: What is __init__.py for?
# A: It's a part of a package.
#   The __init__.py files are required to make Python treat the
#   directories as containing packages; this is done to prevent directories with a common name, such as string,
#   from unintentionally hiding valid modules that occur later (deeper) on the module search path. In the simplest
#   case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the
#   __all__ variable, described later.

