module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:5002',
                changeOrigin: true,
                pathRewrite: { '^/api': '' },
            },
        },
    },
};