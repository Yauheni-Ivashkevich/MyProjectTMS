AGE_1MINUTE = 60
AGE_1HOUR = AGE_1MINUTE * 60
AGE_1DAY = AGE_1HOUR * 24
AGE_1MONTH = AGE_1DAY * 30

MSQ = "Europe/Minsk"

DAYLIGHT = range(9, 21)

SCRIPT_GOOGLE_ANALYTICS = """
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-162140419-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-162140419-1');
</script>
"""

SCRIPT_GOOGLE_TAG_MANAGER_HEAD = """
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MJK77Z9');</script>
<!-- End Google Tag Manager -->
"""

SCRIPT_GOOGLE_TAG_MANAGER_BODY = """
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MJK77Z9"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""

SCRIPT_GOOGLE_TAG_MANAGER = {
    "head": SCRIPT_GOOGLE_TAG_MANAGER_HEAD,
    "body": SCRIPT_GOOGLE_TAG_MANAGER_BODY,
}

SCRIPT_YANDEX_METRIKA = """
<!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");
   ym(61461787, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true,
        webvisor:true
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/61461787" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
"""
