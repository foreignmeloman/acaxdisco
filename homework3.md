1. Write a bash script to be a universal archive extraction tool for the follwoing formats: `tar.gz`, `tar.xz`, `tar.bz2`, `zip`, `whl`. For `zip` and `whl` formats you might need to install `unzip` binary. If the output directory is not given, the current directory should be used.

Expected usage:
```bash
$ script.sh archive_file [output_dir]
```

Archive examples for testing:
* https://github.com/berkerpeksag/astor/archive/refs/tags/0.8.1.tar.gz
* https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.0/lld-12.0.0.src.tar.xz
* https://gitlab.com/linuxcafefederation/awesome-alternatives/-/archive/master/awesome-alternatives-master.tar.bz2
* https://github.com/naiquevin/pipdeptree/archive/refs/heads/master.zip
* https://files.pythonhosted.org/packages/21/58/533fc925de8597e2dd7976f388ec473c5ef6b084d67344febd60a5a20712/pipdeptree-2.1.0-py3-none-any.whl

---

1. Write a script that would scan a directory and print all relative file paths that mention either `Apache License` or `Lesser General Public License`. The result should be printed alphabetically sorted and should not contain repeating entries.

Expected usage:
```
$ script.sh source_dir
```

Example output for `metis-5.1.0` source directory:
```
GKlib/getopt.c
GKlib/gk_mksort.h
GKlib/gkregex.c
GKlib/gkregex.h
LICENSE.txt
```

Archive examples for testing:
* http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz
* lld-12.0.0.src.tar.xz from previous exercise.
