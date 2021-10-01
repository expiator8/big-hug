module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        main_bg: "#F0F2F5",
        post: "#FFFFFF",
        p_edit: "#323334",
        border: "#DBDBDB",
        pg_bd: "#d7d7d7",
        pg_text: "#7d7d7d",
        pg_bg_hov: "#1d1f20",
        pg_text_hov: "#fdfdfd",
      },
      zIndex: {
        '101': -1,
      },
      spacing: {
        'post': '840px',
        'post_edit': '590px',
        'post_type': '58.1px',
        'post_title': '479.1px',
        'post_writer': '151.3px',
        'post_update': '50.5px',
        'post_count': '50.5px',
        'post_like': '50.5px',
        'post_type_in': '50.1px',
        'post_title_in': '471.1px',
        'post_writer_in': '143.3px',
        'post_update_in': '42.5px',
        'post_count_in': '42.5px',
        'post_like_in': '42.5px',
        "25vh": "25vh",
        "50vh": "50vh",
        "75vh": "75vh",
      },
      borderRadius: {
        xl: "1.5rem"
      },
      fontSize: {
        '11': '11px',
        '12': '12px',
        '13': '13px',
      },
      minHeight: {
        "50vh": "50vh",
        "75vh": "75vh"
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
