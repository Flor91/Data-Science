#!/bin/bash

time='date +%H%M%S'

if [[ time < 120000 ]]; then
  greeting='Good Morning'
elif [[ time < 200000 ]]; then
  greeting='Good Afternoon'
else
  greeting='Good Evening'
fi

echo -e "--------------------------------------------------------------------------------"
echo    "***************             ${greeting} Flor!                    **************"
echo -e "--------------------------------------------------------------------------------"

curl -s  'https://quotes.rest/qod?category=students' | \
 jq '.contents.quotes[0].quote','.contents.quotes[0].author'

conda activate dhdsblend

cd ~/Documents/Flor/Data-Science/

echo "Abrir Zoom?"
select yn in "Yes" "No"; do
  case $yn in
     [Yes]* ) echo v2.aula | pbcopy; open -g https://digitalhouse.zoom.us/my/aulavirtual2 &; break;;
     [No]* ) break;;
  esac
done

echo "Abrir playground?"
select yn in "Yes" "No"; do
  case $yn in
     [Yes]* ) open -g https://playground.digitalhouse.com/ar/ &; break;;
     [No]* ) break;;
  esac
done

echo "Abrir carpeta Clases?"
select yn in "Yes" "No"; do
  case $yn in
     [Yes]* ) open -g Clases &; break;;
     [No]* ) break;;
  esac
done

echo "Abrir Jupyter?"
select yn in "Yes" "No"; do
  case $yn in
     [Yes]* ) jupyter lab &; break;;
     [No]* ) break;;
  esac
done


echo Have a good class!