const fs = require('fs');
const path = require('path');

class PaymentParser {
  constructor(filePath) {
    this.filePath = filePath;
    this.parsedData = [];
  }

  async parseFile() {
    try {
      const data = await fs.promises.readFile(this.filePath, 'utf8');
      const lines = data.split('\n');
      for (const line of lines) {
        const payment = this.parseLine(line);
        if (payment) {
          this.parsedData.push(payment);
        }
      }
    } catch (error) {
      throw new Error(`Error parsing file: ${error.message}`);
    }
  }

  parseLine(line) {
    const regex = /^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(\d{1,3}(?:\.\d{3})*(?:,\d+)?)(?:\s+(.*))$/;
    const match = line.match(regex);
    if (match) {
      return {
        date: match[1],
        time: match[2],
        type: match[3],
        amount: parseFloat(match[4].replace(/,/g, '')),
        description: match[5] || ''
      };
    }
    return null;
  }

  getParsedData() {
    return this.parsedData;
  }
}

module.exports = PaymentParser;