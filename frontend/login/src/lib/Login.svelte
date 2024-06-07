<script>
    import {
        Alert,
        Button,
        Checkbox,
        Label,
        Input,
        Spinner,
    } from "flowbite-svelte";

    import Cookies from "js-cookie";

    let email = "";
    let password = "";
    let errorMessageFromServer = "";

    import { useMutation } from "@sveltestack/svelte-query";
    import { login } from "./services/auth.service";

    const loginMutation = useMutation(() => {
        return login(email, password);
    });

    async function onSigIn() {
        try {
            Cookies.remove("currentUser");
            const data = await $loginMutation.mutateAsync();
            if (data === "success") {
                window.location.replace("/app-a/home");
            }
        } catch (err) {
            errorMessageFromServer = err.response.data?.message;
        }
    }
</script>

<div class="container-login">
    <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <form class="flex flex-col space-y-6">
            <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">
                Login
            </h3>
            <Label class="space-y-2">
                <span>Username</span>
                <Input
                    bind:value={email}
                    type="text"
                    name="Username"
                    placeholder="Username"
                    required
                />
            </Label>
            <Label class="space-y-2">
                <span>Your password</span>
                <Input
                    bind:value={password}
                    type="password"
                    name="passwords"
                    placeholder="•••••"
                    required
                    on:keydown={(e) => {
                        if (e.key === "Enter") {
                            onSigIn();
                        }
                    }}
                />
            </Label>
            <div class="flex items-start">
                <Checkbox>Remember me</Checkbox>
            </div>

            <Button
                type="button"
                class="w-full1"
                on:click={onSigIn}
                disabled={email === "" ||
                    password === "" ||
                    $loginMutation.isLoading}
            >
                {#if $loginMutation.isLoading}
                    <Spinner class="mr-3" size="4" />
                {/if}
                Sign in
            </Button>
            {#if $loginMutation.isError}
                <Alert>
                    {errorMessageFromServer || $loginMutation.error}
                </Alert>
            {/if}
        </form>
    </div>
</div>

<style>
    .container-login {
        box-shadow: rgba(17, 12, 46, 0.15) 0px 48px 100px 0px;
        width: 500px;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
    }

    @media only screen and (max-width: 600px) {
        .container-login {
            width: 100%;
        }
    }
</style>
