#!/usr/bin/env bash


echo 'These files will be added to the commit:'
git diff --name-only --cached

echo 'Are you ready? Enter: y/n'
read userStatus

if [[ "$userStatus" == 'y' ]]; then

  while true; do
    echo 'Enter commit message:'
    read commitMessage

    if [[ -z "$commitMessage" ]]; then
      echo "Commit message is required"
    else
      git commit -m "$commitMessage"
      git push
      break
    fi

  done

else
  echo 'Bash script stopped'
fi