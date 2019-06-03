const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    mode: 'development',
    entry: path.join(__dirname, 'assets/src/js/index'),
    output: {
        path: path.join(__dirname, './assets/dist/'),
        filename: '[name]-[hash].js'
    },
    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: 'webpack-stats.json'
        }),
    ],
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader'
                ]
            },
        ],
    },
}
