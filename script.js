const mean = 16.26; 
const stdDev = 14.57; 

document.getElementById('numberForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const numberInput = document.getElementById('numberInput').value;
    const number = parseFloat(numberInput);
    
    if (isNaN(number)) {
        document.getElementById('result').textContent = '請輸入有效的數字。';
        return;
    }
    
    const zScore = (number - mean) / stdDev;
    
    let resultText = '';
    let descrption = '';
    if (zScore >= 2) {
        resultText = 'S';
        descrption = '你這種就是虛解題數，就是刷各種題目增加 AC 數，看上去很強，其實沒什麼用，打個比方吧，就是我和你都上計程，你拿 A+，雖然我停修了，但是我還是不服。';
    } else if(zScore >= 1.3) {
        resultText = 'A';
        descrption = '別再捲了老兄，我們學不動了';
    } else if(zScore >= -0.5) {
        resultText = 'B';
        descrption = '菜雞，在一起，強大';
    } else {
        resultText = 'C';
        descrption = '只有兩種人不刷題的...';
    }
    
    document.getElementById('result').textContent = resultText;
    document.getElementById('result').className = resultText;
    document.getElementById('description').textContent = descrption;
    document.getElementById('info').textContent = `現在資工系 B13 平均 AC 數是：${mean} 標準差是：${stdDev} 而你的標準分數是：${zScore}`;
});
