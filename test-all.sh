find . -name *_test.py | grep -v _site | sort | while read f
do
  echo "*** $f"
  python3 $f
  echo
done