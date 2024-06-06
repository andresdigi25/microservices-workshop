<script>
    import { DarkMode } from "flowbite-svelte";
    import {
        Navbar,
    } from "flowbite-svelte";
</script>

<Navbar let:hidden let:toggle rounded color="form">
    <div class="flex md:order-2">
        <DarkMode />
    </div>
</Navbar>
