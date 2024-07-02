<template>
    <div class="app">
        <Sidebar />
        <div class="content">
            <Header />
            <PageHeader/>
            <router-view class="content_layout" />
        </div>
    </div>
</template>

<script setup>
import Sidebar from "@/components/Sidebar.vue";
import Header from "@/components/Header.vue";
import PageHeader from "@/components/PageHeader.vue";
</script>

<style lang="scss">
:root {
    --primary: #4ade80;
    --primary-alt: #22c55e;
    --grey: #64748b;
    --dark: #1e293b;
    --dark-alt: #334155;
    --light: #f1f5f9;
    --sidebar-width: 300px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Montserrat", sans-serif;
}

body {
    background: var(--light);
}

button {
    cursor: pointer;
    appearance: none;
    border: none;
    outline: none;
    background: none;
}

.app {
    display: flex;
    .content_layout {
        padding: 1rem;
        width: 100%;
    }
}

.content {
    width: 100%;
    @media (max-width: 1024px) {
        padding-left: 4rem;
    }
}
</style>
