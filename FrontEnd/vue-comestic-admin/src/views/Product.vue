<template>
    <a-space warp>
        <a-button type="primary" class="btn_add" block>Thêm sản phẩm</a-button>
        <a-button type="primary" danger>Xoá sản phẩm</a-button>
    </a-space>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getCategory } from "@/services/product.service";

const data = ref(null);

onMounted(async () => {
    try {
        const response = await getCategory();
        data.value = response.data;
        console.log(response);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
});

</script>

<style lang="scss" scoped>
.btn_add {
    background-color: #00cc00 !important;
    border-color: #00cc00 !important;
}

.btn_add:hover,
.btn_add:focus {
    background-color: #339900 !important;
    border-color: #339900 !important;
}
</style>
