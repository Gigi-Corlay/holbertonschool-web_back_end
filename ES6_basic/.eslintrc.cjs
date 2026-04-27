module.exports = {
    env: {
      es6: true,
      node: true,
      jest: true,
    },
    extends: 'airbnb-base',
    parserOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
    },
    plugins: ['jest'],
    rules: {
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
      ],
    },
  };
  