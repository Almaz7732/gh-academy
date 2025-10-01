# Solution

## Step 1: Create a Directory
```bash
mkdir week_one
```

## Step 2: Navigate to the Directory
```bash
cd week_one
```


## Step 3: Create a Text File
```bash
touch hw.txt
```

## Step 4: Add Text Content to the File
```bash
echo "Evolution of computer systems
Computers are programmable electronic devices that can process data. To comprehend what a computer system is, it's important to analyze the history and evolution of computer system development over the years." > hw.txt
```

## Step 5: Replace Text Using Sed
```bash
sed 's/computer/IT/g' hw.txt
```