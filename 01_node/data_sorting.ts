/**
 * Q:
 * Write a function or code snippet that organizes and records
 * metadata from audio and video files located within the `files` object
 *
 * Write your code below.
 */

const saveToDb = async (
  category: 'audio' | 'videos',
  data: {
    trackTitle: string;
    filePath: string;
    genre: string;
  },
) => {
  return new Promise((resolve, reject) => {
    resolve(true);
  });
};

const files = [
  '/tmp/files/rock/title1.mp3',
  '/tmp/files/soul/title2.mp4',
  '/tmp/files/rock/title5.mp4',
  '/tmp/files/pop/title4.mp3',
  '/tmp/files/pop/title6.mp3',
  '/tmp/files/country/title7.mp3',
  '/tmp/files/country/title8.mp4',
  '/tmp/files/pop/title9.mp4',
  '/tmp/files/jazz/title10.mp3',
  '/tmp/files/pop/title11.mp3',
];
