<script>
    import Login from "./lib/Login.svelte";
    import Navbar from "./lib/Navbar.svelte";
    import { Router, Route } from "svelte-routing";
    import Notfound from "./lib/Notfound.svelte";
    import ThemeStore from "./lib/Store";
    import {
        QueryClient,
        QueryClientProvider,
    } from "@sveltestack/svelte-query";

    const queryClient = new QueryClient({
        defaultOptions: {
            queries: {
                refetchOnWindowFocus: false,
            },
        },
    });
    export let url = "";

    function detectThemeChange() {
        ThemeStore.set({
            theme: localStorage.getItem("color-theme"),
        });
    }
</script>

<QueryClientProvider client={queryClient}>
    <main>
        <Router {url} basepath="/svelte">
            <!-- svelte-ignore a11y-no-static-element-interactions -->
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <section on:click={detectThemeChange}>
                <Navbar />
            </section>

            <div class="md:container md:mx-auto mt-10">
                <Route path="/non-sso-login"><Login /></Route>
                <Route path="*"><Notfound /></Route>
            </div>
        </Router>
    </main>
</QueryClientProvider>
