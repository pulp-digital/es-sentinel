**/configure:
  order compiler
  trace no
**/do-prebuild:
  order compiler
  trace no
**/as:
**/*-as:
  invoke ${config_dir}/extractor
  order compiler, extractor
  prepend --assembler
  prepend --codeql-assembler-executable
  prepend ${compiler}
**/collect2:
  invoke ${config_dir}/extractor
  order compiler, extractor
  prepend --linker
  prepend --semmle-linker-executable
  prepend ${compiler}
**/ld*:
**/*-ld*:
**/lld*:
  invoke ${config_dir}/extractor
  order compiler, extractor
  prepend --linker
  prepend --semmle-linker-executable
  prepend ${compiler}
**/armlink:
  invoke ${config_dir}/extractor
  order compiler, extractor
  prepend --arm-linker
  prepend --semmle-linker-executable
  prepend ${compiler}
**/*clang*:
**/*cc*:
**/*++*:
**/icpc:
  invoke ${config_dir}/extractor
  order compiler, extractor
  prepend --mimic
  prepend ${compiler}
/usr/bin/codesign:
  replace yes
  invoke /usr/bin/env
  prepend /usr/bin/codesign
  trace no
/usr/bin/pkill:
  replace yes
  invoke /usr/bin/env
  prepend /usr/bin/pkill
  trace no
/usr/bin/pgrep:
  replace yes
  invoke /usr/bin/env
  prepend /usr/bin/pgrep
  trace no
