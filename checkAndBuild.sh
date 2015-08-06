while true; do

  inotifywait .*
  ./buildScript.py Abschlussarbeit.tex out/


done