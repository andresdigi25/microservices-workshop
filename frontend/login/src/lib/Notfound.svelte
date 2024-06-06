<script>
    import { Link } from "svelte-routing";
</script>

<div
    class="lg:px-24 lg:py-24 md:py-20 md:px-44 px-4 py-24 items-center flex justify-center flex-col-reverse lg:flex-row md:gap-28 gap-16"
>
    <div class="xl:pt-24 w-full xl:w-1/2 relative pb-12 lg:pb-0">
        <div class="relative">
            <div class="absolute">
                <div class="" />
            </div>
            <div>
                <img alt="notfound" src="https://i.ibb.co/G9DC8S0/404-2.png" />
                <Link to="/svelte/non-sso-login">
                    <button
                        class="lg:w-auto my-2 border rounded md py-4 px-8 text-center bg-indigo-600 text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-700 focus:ring-opacity-50"
                    >
                        Go login!
                    </button>
                </Link>
            </div>
        </div>
    </div>
    <div>
        <img alt="group" src="https://i.ibb.co/ck1SGFJ/Group.png" />
    </div>
</div>
