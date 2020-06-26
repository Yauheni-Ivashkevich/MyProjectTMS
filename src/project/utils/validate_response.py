from typing import Callable
from typing import Collection
from typing import Dict
from typing import List
from typing import Optional


class TemplateResponseTestMixin:
    def validate_response(
        self,
        *,
        url: str,
        client: Optional = None,
        method: Optional[str] = "get",
        form_data: Optional[Dict] = None,
        expected_status_code: Optional[int] = 200,
        expected_view: Optional[type] = None,
        expected_view_name: Optional[str] = None,
        expected_template: Optional[str] = None,
        content_filters: Optional[Collection[Callable[[bytes], bool]]] = None,
        expected_redirect_chain: Optional[List] = None,
    ):
        cli = client or self.client
        meth = getattr(cli, method)

        meth_args = []
        if form_data:
            meth_args.append(form_data)

        resp = meth(url, *meth_args, follow=True)
        self.assertEqual(expected_status_code, resp.status_code, f"bad status code")

        if expected_redirect_chain is not None:
            self.assertEqual(
                expected_redirect_chain, resp.redirect_chain, f"bad redirect chain"
            )

        good_resolver_codes = {
            200,
        }

        if expected_status_code in good_resolver_codes:
            self.assertEqual(
                expected_view_name, resp.resolver_match.view_name, f"bad view name",
            )
            self.assertEqual(
                expected_view.as_view().__name__,
                resp.resolver_match.func.__name__,
                "bad view class/function name",
            )

            if expected_template is not None:
                self.assertIn(
                    expected_template, resp.template_name, f"bad template",
                )

        for content_filter in content_filters or []:
            content = resp.content
            self.assertTrue(
                content_filter(content),
                f"content filter {content_filter} failed: content=`{content}`",
            )
