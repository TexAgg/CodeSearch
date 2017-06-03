#! /bin/bash
# http://bit.ly/2ryNqxM

yarn install
# http://bit.ly/2qzZLx2
node_modules/.bin/lessc --clean-css "Content/Styles/main.less" "dist/main.css"