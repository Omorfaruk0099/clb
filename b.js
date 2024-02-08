const TelegramBot = require('node-telegram-bot-api');
const { exec } = require('child_process');
const shellQuote = require('shell-quote');

// Telegram bot token
const token = '6311954830:AAFelhOxi5GkzecWwiQIccxvXnfc1rppOQI';
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/attack (.+)/, (msg, match) => {
  const chatId = msg.chat.id;
  const target = match[1];
  const escapedTarget = shellQuote.quote([target]);

  exec(`node att.js ${escapedTarget}`, (error, stdout, stderr) => {
    if (error) {
      bot.sendMessage(chatId, `Error occurred: ${error.message}`);
      return;
    }
    if (stderr) {
      bot.sendMessage(chatId, `Error log: ${stderr}`);
      return;
    }
    bot.sendMessage(chatId, '😈 ATTACK BY MD OMOR FARUK 😈');
  });
});
