#!/usr/bin/node
// This script computes the number of tasks completed by user id

const request = require('request');
request(process.argv[2], function (err, data, body) {
  if (!err) {
    const tasks = JSON.parse(body);
    const complete = {};
    tasks.forEach((task) => {
      if (task.completed && complete[task.userId] === undefined) {
        complete[task.userId] = 1;
      } else if (task.completed) {
        complete[task.userId] += 1;
      }
    });
    console.log(complete);
  }
});
