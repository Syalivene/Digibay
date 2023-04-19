/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./app002/templates/app002/base.html",
      "./app002/templates/app002/login.html",
      "./app002/templates/app002/signup.html",
      "./app002/templates/app002/index.html",
      "./app002/templates/app002/profile.html",
      "./conversation/templates/conversation/new.html",
      "./conversation/templates/conversation/detail.html",
      "./conversation/templates/conversation/inbox.html",
      "./item/templates/item/detail.html",
      "./item/templates/item/form.html",
      "./item/templates/item/multiple_filter_items.html",
      "./dashboard/templates/dashboard/boutique.html",
      "./dashboard/templates/dashboard/index.html",
      "./dashboard/templates/dashboard/market.html",
      "./static/javascript/app002.js",
      "./static/javascript/conversation.js",
      "./static/javascript/item.js",
      ],
  theme: {
    extend: {},
  },
  plugins: [],
}

