echo "Entering directory /PythOS"
cd /PythOS
echo Done
echo "Resetting cache file"
rm -rf /PythOS/PythOS/boot/yn.txt
echo "Done"
echo "Writing cache file"
echo "False" > /PythOS/PythOS/boot/yn.txt
echo "Done"
fcontent=$(cat /PythOS/PythOS/boot/yn.txt)
echo "Starting PythOS virtual environment"
source venv/bin/activate
echo "Done"

echo "Entering main"
python3 main.py

clear
